# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for Tkinter and any other necessary packages
RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get install -y tcl8.6 tk8.6 && \
    apt-get install -y build-essential && \
    apt-get install -y libffi-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y libbz2-dev && \
    apt-get install -y zlib1g-dev && \
    apt-get install -y libreadline-dev && \
    apt-get install -y libsqlite3-dev && \
    apt-get install -y wget && \
    apt-get install -y curl && \
    apt-get install -y llvm && \
    apt-get install -y libncurses5-dev && \
    apt-get install -y libncursesw5-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the display variable for GUI applications (if needed)
ENV DISPLAY=:0

# Make port 5000 available to the world outside this container (if your app runs on a specific port)
EXPOSE 5000

# Run weather.py when the container launches
CMD ["python", "weather.py"]
