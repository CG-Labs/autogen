# Use the official Python image from the Docker Hub
FROM python:3.9

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the entire AutoGen framework into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /usr/local/lib/python3.9/site-packages:/app:/app/autogen

# Keep the container running indefinitely
CMD ["tail", "-f", "/dev/null"]
