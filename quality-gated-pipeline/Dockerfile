# Stage 1: Build/Test stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run tests
# hiddden this command - 'RUN pytest tests/''
RUN python -m pytest tests/

# Stage 2: Final Runtime stage
FROM python:3.11-slim

WORKDIR /app

# FIX: Change 'requirements-stage' to 'builder'
COPY --from=builder /app/app ./app
COPY --from=builder /app/requirements.txt . 

# Copy dependencies and main entry point
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app/app/app.py .

EXPOSE 5000

# Run the application
CMD ["python", "app.py"]