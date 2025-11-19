FROM python:3.10-slim-bullseye

WORKDIR /app

# Install system deps, then clean apt lists
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps using build cache-friendly steps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

CMD ["python3", "app.py"]