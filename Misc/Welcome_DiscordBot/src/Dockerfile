# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# Define environment variable
ENV DISCORD_TOKEN your_token_here
ENV DISCORD_CHANNEL_ID your_channel_id_here

# Run bot.py when the container launches
CMD ["python", "./bot.py"]
