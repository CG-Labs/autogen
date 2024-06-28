# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Set PYTHONPATH environment variable
ENV PYTHONPATH /usr/local/lib/python3.9/site-packages

# Run web_scraping_tool.py when the container launches
CMD ["python", "web_scraping_tool.py"]
