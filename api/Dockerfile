# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Run alembic migrations
# The DATABASE_URL will be passed as an argument during the build process or will be available as an environment variable
# For now, we assume the user will run migrations manually or as part of an entrypoint script.
# RUN alembic upgrade head

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches
# Use uvicorn to run the app. The --host 0.0.0.0 is important to make it accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
