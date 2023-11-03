# Blogzart!

## Description

**Blogzart!** is a comprehensive Flask-based blogging platform tailored for ease of use and rich functionality. It provides a creative outlet for content creators and an interactive space for readers to engage with posts.

## Features

### Live Features
- **User Authentication**: Robust sign-up and login features to manage user accounts.
- **Likes System**: Users can show their appreciation for content by liking posts.
- **Comment System**: Engage with the community through comments on blog posts.
- **Rich Text Editor**: Utilizes CKEditor to enable detailed content creation.
- **Responsive Design**: Ensures a smooth experience on all devices using Flask-Bootstrap.
- **Gravatar Integration**: Displays personalized user avatars.
- **Email Integration**: Supports email operations for user interactions and notifications.
- **Admin Dashboard**: Equipped for site administrators to manage posts and users effectively.

### Future Enhancements
- **AI-Based Comment Moderation**: We are excited to be working on an LSTM RNN model to intelligently moderate comments, ensuring conversations remain respectful and relevant.

## Getting Started

### Prerequisites
Make sure you have Python 3.6+ and pip installed on your machine.

### Installation

```bash
# Clone the Blogzart! repository
git clone https://github.com/rakibulhaque9954/blog_remastered

# Navigate to the project directory
cd path-to-Blogzart

# Install the required dependencies
pip install -r requirements.txt

# Set up environment variables
export MY_EMAIL='your-email@example.com'
export APP_PASSWORD='your-email-app-password'
export SECRET_KEY='your-secret-key'

# Initialize the database
flask db init
flask db migrate
flask db upgrade

# Launch the server
flask run
Visit http://localhost:5000 in your browser to start using Blogzart!
```

## Codebase Overview

### server.py
Serves as the backbone of the application, setting up the server, routes, and integrating Flask extensions.

### index_try.html
Acts as the main landing page template, incorporating logic for displaying different content based on user authentication and providing areas for dynamic content such as comments and likes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback about Blogzart!, please open an issue in the GitHub repository.

## Acknowledgments

Immense gratitude to all the open-source contributors and the community for their ongoing support and inspiration that have helped shape Blogzart!.
