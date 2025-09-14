# Use official Python image as base
FROM python:3.13-slim-trixie

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements file, install Python dependencies
COPY requirements.txt .
RUN pip install uv
RUN uv pip install -r requirements.txt --no-cache-dir


# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
