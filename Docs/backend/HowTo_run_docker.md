
## Dockerfile


docker build -t fastapi_app .

docker run -p 8000:8000 -d fastapi_app

docker run -it fastapi_app bash


## Docker compose


docker-compose up --build -d

docker-compose down



