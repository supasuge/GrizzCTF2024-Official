# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the Flask application to the working directory
COPY app.py .
COPY flag.txt .

# Expose the port on which the Flask application will run
EXPOSE 10000

# Set the command to run the Flask application
CMD ["python", "app.py"]