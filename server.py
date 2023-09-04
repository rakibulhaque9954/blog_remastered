import datetime
import random
import time
from functools import wraps
import werkzeug.security
from sqlalchemy.orm import relationship
from flask_wtf.csrf import CSRFProtect
from random_wallpapers import wallpapers
from forms import RegisterUser, CreatePostForm, LoginForm, CommentForm
from flask import Flask, render_template, request, redirect, url_for, flash, session, get_flashed_messages, abort, jsonify
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
import smtplib
import os

email = os.environ.get('MY_EMAIL')
app_password = os.environ.get('APP_PASSWORD')

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)

"""Gravatar initialisation(basically avatars made by creating hash from associated emails"""
gravatar = Gravatar(app, size=20, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False,
                    base_url=None)

"""Login Manager Initialised"""
login_manager = LoginManager()
login_manager.init_app(app)

"""Connect to db"""
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

"""Configure table"""


class BlogPost(db.Model):
    """blog_post db Schema"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)

    """one to many relation with user"""
    # foreign key where author_id = user_id of the user that created the post
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # a reference of user_object in Blogpost table
    author = relationship("User", back_populates="posts")

    """one to many relation with comments one from blog to multiple comments reference"""
    comments = relationship("Comment", back_populates="post")
    img_url = db.Column(db.String(250), nullable=False)

    """one to many relation with Likes"""
    likes = relationship("Like", back_populates="post")

    def __repr__(self):
        return f'Post {self.title}'

    def to_dict(self, user):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def is_liked_by(self, user):
        for like in self.likes:
            if like.user_id == user.id:
                return True
        return False


"""User Table"""
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    posts = relationship("BlogPost", back_populates="author")
    comment = relationship("Comment", back_populates="comment_user")

    """one to many relation with Likes"""
    likes = relationship("Like", back_populates="user")

    def __repr__(self):
        return f'{self.name} user added to db...'


"""Comments Table"""
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Text, nullable=False)

    """one to many relation with user"""
    comment_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comment_user = relationship("User", back_populates="comment")

    """one to many relation with BlogPost"""
    blog_post_id = db.Column(db.Integer, db.ForeignKey("blog_post.id"))
    post = relationship("BlogPost", back_populates="comments")


"""Like Table"""
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    """Foreign keys"""
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_Id = db.Column(db.Integer, db.ForeignKey("blog_post.id"))

    user = relationship("User", back_populates="likes")
    post = relationship("BlogPost", back_populates="likes")


with app.app_context():
    db.create_all()

"""decorator for admin only"""


def admin_only(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            # If the user is not logged in, redirect to a non-privileged page (e.g., home page)
            return abort(404, "Sorry out of bounds")

        if not current_user.is_admin:
            # If the user is not an admin, redirect to a non-privileged page (e.g., home page)
            return abort(404, "Sorry admin privileges only")
        return view_func(*args, **kwargs)

    return decorated_view


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home_page():
    """Home page for the blog"""
    results = BlogPost.query.all()
    wallpaper = random.choice(wallpapers)
    # """Using list comprehension for better code"""
    # posts = [result.to_dict() for result in results]

    return render_template('index_try.html', posts=results, logged_in=current_user.is_authenticated,
                           wallpaper=wallpaper)


@app.route('/blog/<index>', methods=['GET', 'POST'])
def post(index):
    """Post page of the blog"""
    """Comment form"""
    form = CommentForm()
    result = BlogPost.query.get(index)

    if request.method == 'POST' and not current_user.is_authenticated:
        session.pop('_flashes', [])
        flash('Please Login or register to comment', 'error')
        return redirect(url_for('login'))
    elif request.method == 'POST' and form.validate_on_submit():
        new_comment = Comment(
            comments=form.body.data,
            comment_user=current_user,
            post=result

        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('post', index=result.id))

    return render_template('post.html', post_s=result, logged_in=current_user.is_authenticated, form=form)


@app.route('/toggle_like/<int:post_id>', methods=['POST'])
@login_required
def toggle_like(post_id):
    post = BlogPost.query.get_or_404(post_id)
    user = current_user

    # Check if the user has already liked the post
    like = Like.query.filter_by(post=post, user=user).first()

    if like:
        # User has already liked the post, so remove the like
        db.session.delete(like)
        db.session.commit()
    else:
        # User has not liked the post, so add the like
        new_like = Like(user=user, post=post)
        db.session.add(new_like)
        db.session.commit()

    total_likes = Like.query.filter_by(post=post).count()
    liked = True if like else False  # Check if the user has liked the post after the toggle

    return jsonify({'liked': liked, 'total_likes': total_likes})


@app.route('/blog/posts/new-post', methods=['GET', 'POST'])
@admin_only
@login_required
def new_post():
    """Creates new post using RESTful api GET & POST"""
    form = CreatePostForm()
    time_now = datetime.datetime.now()
    if request.method == 'POST' and form.validate_on_submit():
        new_blog_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=str(time_now.strftime(f"%B %d, %Y")),
            body=form.body.data,
            img_url=f"{form.img_url.data}",
            author=current_user
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template('new_post.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/blog/posts/edit-post', methods=['GET', 'POST'])
@admin_only
@login_required
def edit_post():
    """Edit's Current post using RESTful api using GET and POST"""
    post_id = request.args.get('post_id')
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if request.method == 'POST' and edit_form.validate_on_submit():
        """Be Careful in adding commas as it can lead to tuples being created unnecessarily and debugging for hours"""
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.date = post.date
        post.body = edit_form.body.data
        post.img_url = f"{edit_form.img_url.data}"
        post.author = edit_form.author.data
        db.session.commit()
        return redirect(url_for('post', index=post_id))

    return render_template('edit_post.html', form=edit_form, logged_in=current_user.is_authenticated)


@app.route('/delete', methods=['GET'])
@admin_only
@login_required
def delete_post():
    """Deletes post from the db and redirect to homepage"""
    post_id = request.args.get('post_id')
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home_page'))


@app.route('/delete-comment')
@login_required
def delete_comment():
    comment_id = int(request.args.get('comment_id'))
    comment_to_delete = Comment.query.get(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('post', index=int(request.args.get('post_id'))))


@app.route('/blog/about')
def about():
    """About me page"""
    return render_template('about.html', logged_in=current_user.is_authenticated)


@app.route('/blog/contact_me')
def contact_me():
    """Contact me form"""
    return render_template('contact.html', logged_in=current_user.is_authenticated)


@app.route('/sent_message', methods=['POST'])
def sent():
    """Gets data and redirects data using SMPTPLIB Module to my Email"""
    name = request.form['name']
    email_address = request.form['email']
    phone_number = request.form['phone_number']
    message = request.form['message']
    sender_email = os.environ.get('sender_email')
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=app_password)
        connection.sendmail(from_addr=email, to_addrs=sender_email,
                            msg=f'Subject: Message from Blog\n\nName: {name}\nEmail: {email_address}\n'
                                f'Phone Number: {phone_number}\nMessage: {message}')
    return render_template('sent_success.html')


@app.route('/register_user', methods=['GET', 'POST'])
def register():
    form = RegisterUser()

    password = request.form.get('password')
    if request.method == 'POST' and form.validate_on_submit():
        if not User.query.filter_by(email=request.form.get('email')).first():
            hashed_password = werkzeug.security.generate_password_hash(password, method="pbkdf2:sha256", salt_length=10)
            new_user = User(
                name=request.form.get('name'),
                email=request.form.get('email'),
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            session.pop('_flashes', [])
            print("Flash Messages:", get_flashed_messages())
            flash('Registration Successful', 'success')
            flash('Please Login from here', 'success')
            return redirect(url_for('login'))
        else:
            session.pop('_flashes', [])
            flash('User already exists, Please Login', 'error')

    return render_template('register.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global first
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            first = True
            if werkzeug.security.check_password_hash(pwhash=user.password, password=request.form.get('password')):
                login_user(user)
                session.pop('_flashes', [])
                return redirect(url_for('home_page'))
            else:
                session.pop('_flashes', [])
                flash('Wrong Password, Try Again', 'error')
        else:
            session.pop('_flashes', [])
            flash('The Email is not registered', 'error')
    return render_template('login.html', form=form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    """Clear flash cache and prevents from repeating the same flash message again"""
    session.pop('_flashes', [])
    flash('logged out successfully', 'success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
