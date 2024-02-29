# Use the official Python image for ARM architecture from the Docker Hub
FROM arm32v7/python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Add Google Chrome's repository to the sources list
RUN echo 'deb [arch=armhf] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome for ARM architecture
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean

# Expose the WebSocket port
EXPOSE 8765

# Run the WebSocket server when the container starts
CMD ["python3", "websocket_fol/api.py"]
