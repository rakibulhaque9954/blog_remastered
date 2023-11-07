# Blogzart 2.0!
[日本語](https://github.com/rakibulhaque9954/blog_remastered/blob/74bf117f4576450b8eae2b658ca1273c2e529dc4/%E6%97%A5%E6%9C%AC%E8%AA%9EREADME.md)

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

- **AI-Based Comment Moderation**: The LSTM RNN model, hosted on GCP, moderates comments in real-time through RESTful API calls from the main blog platform hosted on Render. This integration ensures efficient and scalable comment moderation with a 99% accuracy rate.
- **Here is the Repository**: [Click here](https://github.com/rakibulhaque9954/Comment_Flag_LSTM_Model.git)

## What's New in Blogzart 2.0

- **Cloud-Powered AI Moderation**: Blogzart now harnesses the power of cloud computing with the LSTM-based flagger deployed on GCP. This allows for high-availability and low-latency responses to comment submissions.
- **RESTful API Integration**: The platform uses RESTful API requests from the main blog hosted on Render to perform comment analysis, providing a seamless experience for users and maintaining the integrity of discussions.
- **Scalable Architecture**: The use of GCP for hosting our AI model ensures that Blogzart can handle increased traffic and comment volume without compromising performance.

## Deployed on GCP

Blogzart’s AI moderation system is built with Flask and hosted on Google Cloud Platform, leveraging its managed services to ensure high performance and availability. The RESTful API allows the main blog, hosted on Render, to communicate with the AI model seamlessly, offloading the heavy lifting of comment analysis to the cloud. This approach ensures that the user experience remains fast and responsive, even as the platform grows.

![toxic comment](https://github.com/rakibulhaque9954/blog_remastered/blob/adc3cb260e2fc032a888f194fe0fc02e048dda5e/comment.png)
*Toxic Comment*

![flagged messages](https://github.com/rakibulhaque9954/blog_remastered/blob/adc3cb260e2fc032a888f194fe0fc02e048dda5e/flagged%20message.png)
*Flagged Messages*

Stay tuned for further updates as we continue to enhance the Blogzart experience!

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
```
Visit http://localhost:5000 in your browser to start using Blogzart!


## Codebase Overview

### server.py
Serves as the backbone of the application, setting up the server, routes, and integrating Flask extensions.

### index_try.html
Acts as the main landing page template, incorporating logic for displaying different content based on user authentication and providing areas for dynamic content such as comments and likes.

## License

This project is licensed under the MIT License - see the [License](https://github.com/rakibulhaque9954/blog_remastered/blob/2067516a1ceb3aff915fc2cd47be07df46cf7bb6/MIT_LICENSE_Rakibul_Haque.txt) file for details.

## Contact

If you have any questions or feedback about Blogzart!, please open an issue in the GitHub repository.

## Acknowledgments

Immense gratitude to all the open-source contributors and the community for their ongoing support and inspiration that have helped shape Blogzart!.
