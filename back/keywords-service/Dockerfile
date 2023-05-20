# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the Docker container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container
COPY ../requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 16460

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application when the container launches
CMD ["flask", "run"]
