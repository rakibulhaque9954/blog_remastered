from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class RegisterUser(FlaskForm):
    """Class for a New_users form"""
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


class CreatePostForm(FlaskForm):
    """Class for a New_Post form"""
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image Url", validators=[DataRequired(), URL()])
    body = CKEditorField("Body Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class LoginForm(FlaskForm):
    """Class for a login_form"""
    email = StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    show_password = BooleanField('Show Password', default=False)  # Add the show_password checkbox
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    """Class for comments form"""
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")