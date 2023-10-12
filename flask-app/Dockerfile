# Use an official Python runtime as a parent image
FROM python:3.10.8-slim-bullseye

# Install MySQL client, Chrome and dependencies
RUN apt-get update && apt-get install default-mysql-client libmariadb-dev-compat  build-essential gnupg wget -y && \
  wget --quiet --output-document=- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google-archive.gpg && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get update && \
  apt-get install google-chrome-stable -y --no-install-recommends && \
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

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run Waitress when the container launches
CMD ["waitress-serve", "--port=8080", "app:app"]