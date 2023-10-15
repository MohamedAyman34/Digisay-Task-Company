
# Use an official Python runtime as a parent image
FROM python:3.11.4-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONONDONTWRITEBYTECODE 1

# packages for dockerization
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app/

RUN pip install --upgrade pip 

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .
RUN pip install -r requirements.txt



# Start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]