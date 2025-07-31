# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install docker client
RUN apt-get update && apt-get install -y docker.io

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Run the celery worker when the container launches
# The worker will connect to the Redis broker specified in the .env file
CMD ["celery", "-A", "main.celery", "worker", "--loglevel=info"]
