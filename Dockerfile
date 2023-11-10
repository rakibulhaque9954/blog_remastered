# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

# Copy the current directory contents into the container at /app
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 server:app
