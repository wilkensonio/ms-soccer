# Use the official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app

# Expose the port the app will run on
EXPOSE 8000

# Set environment variables for the app (optional)
ENV DB_HOST=your-db-host
ENV DB_USER=your-db-user
ENV DB_PASSWORD=your-db-password
ENV DB_NAME=your-db-name
ENV DB_PORT=your-db-port

# Command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
