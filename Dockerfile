# Use an official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install -q -U google-generativeai   

# Copy the application files to the container
COPY . .

# Expose the port your application runs on
EXPOSE 8000

# Command to run your application
CMD ["python3", "app.py"]