# Use a base image with Python (official Python image)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt file to the container
COPY requirements.txt .

# Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port (in case of a web application, FastAPI example)
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
