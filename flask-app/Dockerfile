# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install default MySQL client
RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Install libmariadb-dev-compat
RUN apt-get update && \
    apt-get install -y libmariadb-dev-compat && \
    rm -rf /var/lib/apt/lists/*

# Install GCC compiler
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables for MySQL client
ENV DB_HOST=localhost \
    DB_USER=root \
    DB_PASSWORD=secret

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]