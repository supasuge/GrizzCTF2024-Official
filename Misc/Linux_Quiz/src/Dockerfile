FROM python:3.10-slim

# Create a non-root user
RUN grizzctf -D grizzctf

# Set working directory
WORKDIR /app

# Copy the Python quiz script into the container
COPY quiz.py /app/

# Switch to the non-root user 
USER grizzctf

# Expose the quiz server's port
EXPOSE 13337

# Start the quiz server 
CMD ["python", "quiz.py"]
