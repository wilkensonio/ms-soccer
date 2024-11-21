# Use the official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

COPY .env /app/.env

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app

# Expose the port the app will run on
EXPOSE 8000 


# Command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
