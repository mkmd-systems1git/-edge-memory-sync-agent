# Use a secure, official, hyper-lightweight Python runtime to guarantee zero resource bloat
FROM python:3.9-slim

# Establish the secure internal application directory inside the container
WORKDIR /app

# Copy the application source code files into the container image
COPY src/ ./src/

# Force output to stream in real-time straight to system logs without buffering
ENV PYTHONUNBUFFERED=1

# Execute the application engine as the default runtime command
CMD ["python", "src/agent.py"]
