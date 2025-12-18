# 1. Base image with Python installed
FROM python:3.12-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# 4.  Copy application code into container
COPY main.py .

# 5. Expose application port
EXPOSE 8000

# 6. Start FastAPI application 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


