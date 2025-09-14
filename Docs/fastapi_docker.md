# How to Deploying a FastAPI application with Docker and Nginx as a reverse proxy

AI Overview
Deploying a FastAPI application with Docker and Nginx as a reverse proxy involves several steps to containerize your application and manage traffic efficiently.

1. Prepare your FastAPI Application:
  - Create your FastAPI application file (e.g., main.py).
  - Create a requirements.txt file listing all Python dependencies.

2. Dockerize your FastAPI Application:
  - Create a Dockerfile to build an image for your FastAPI application. This typically involves:
    - Using a Python base image.
    - Setting a working directory.
    - Copying requirements.txt and installing dependencies.
    - Copying your application files.
    - Defining the command to run your FastAPI app with an ASGI server like Uvicorn (e.g., CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]).

3. Configure Nginx as a Reverse Proxy:
  - Create an nginx.conf file to configure Nginx. This file will define a server block that listens on a public port (e.g., 80) and proxies requests to your FastAPI container.
  - e.g. 

```
server {
	listen 80;
	server_name your_domain_or_ip; # Replace with your domain or IP

	location / {
		proxy_pass http://fastapi_app:8000; # 'fastapi_app' is the service name in docker-compose
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
	}
}
```

4. Use Docker Compose for Orchestration:
  - Create a docker-compose.yml file to define and run both your FastAPI application and Nginx as separate services.

```
version: '3.8'
services:
  fastapi_app:
	build: .
	ports:
	  - "8000:8000" # Expose port 8000 for internal communication
	restart: always

  nginx:
	image: nginx:latest
	ports:
	  - "80:80" # Expose port 80 to the host
	volumes:
	  - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
	depends_on:
	  - fastapi_app
	restart: always
```

5. Deploy and Run:
  - Build and run your containers using Docker Compose:
```
  docker-compose up --build -d
```


The FastAPI application will now be accessible through Nginx on port 80 of your host machine, forwarding requests to the FastAPI container.



## See Also

- https://medium.com/@hassaan.saleem0214/a-basic-fastapi-microservice-folder-structure-01a05da43f5b
- https://medium.com/@amirm.lavasani/how-to-structure-your-fastapi-projects-0219a6600a8f

