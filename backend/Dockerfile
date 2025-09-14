# Use official Python image as base
FROM python:3.13-slim-trixie

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
# Create a virtual environment in /opt/venv
RUN uv venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin
# Set working directory
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
# Copy requirements file, install Python dependencies
COPY requirements.txt .
RUN uv pip install -r requirements.txt --no-cache-dir


# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
