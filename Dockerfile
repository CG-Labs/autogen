# Use the official Python image from the Docker Hub
FROM python:3.9

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create the /app/coding directory and copy the code_executor_integration.py and web_scraping_tool.py scripts into it
RUN mkdir -p /app/coding && cp /app/code_executor_integration.py /app/coding/ && cp /app/web_scraping_tool.py /app/coding/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Comment out the PYTHONPATH environment variable
# ENV PYTHONPATH /usr/local/lib/python3.9/site-packages:/app:/app/autogen

# Keep the container running indefinitely
CMD ["tail", "-f", "/dev/null"]
