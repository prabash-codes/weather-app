FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app/

RUN pwd
RUN ls


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the display variable for GUI applications
ENV DISPLAY=:0

# Install dependencies for running Tkinter in Docker
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb
# Run the command to start Xvfb and the Tkinter application
CMD ["sh", "-c", "Xvfb :0 -screen 0 1024x768x16 & python weather.py"]