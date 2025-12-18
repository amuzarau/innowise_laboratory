Dockerized FastAPI Application

This project demonstrates how to dockerize a simple FastAPI application and verify that it runs correctly inside a Docker container using a healthcheck endpoint.
The application exposes a single endpoint that returns a JSON response and is used to validate container startup and networking.


📁 Project Structure
lecture_6/
│
├── main.py          # FastAPI application
├── Dockerfile       # Docker configuration
├── .gitignore       # Git ignored files
├── .dockerignore    # Docker ignored files
└── README.md        # Project documentation



🚀 Application Overview

The FastAPI app defines a single endpoint:
GET /healthcheck

Response:
{
  "status": "ok"
}

This endpoint is used to confirm that:
- the application is running
- the Docker container started successfully

The implementation can be found in main.py 

🧰 Requirements
- Docker (Docker Desktop or Docker Engine)
- No local Python installation required (runs fully inside Docker)

🐳 Docker Instructions

1️⃣ Build Docker Image
From the project directory, run:
docker build . -t app:latest
This command creates a Docker image named app.

2️⃣ Verify Image Creation
docker images
You should see app listed in the output.

3️⃣ Run the Container
docker run -p 8000:8000 app:latest
The container will start the FastAPI application.

4️⃣ Check Running Containers
In another terminal:
docker ps

5️⃣ Test the Healthcheck Endpoint
Open your browser 
or use curl:
curl http://localhost:8000/healthcheck

Expected response:
{"status":"ok"}

6️⃣ Access the Container Shell (Optional)
docker exec -it <container-id> bash
This allows you to inspect the container filesystem using ls, cd, etc.

7️⃣ Stop the Container
docker stop <container-id>

Verify stopped containers:
docker ps -a
