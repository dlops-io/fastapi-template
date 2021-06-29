# FastAPI Service Template

## Prerequisites
* Have Docker installed
* Cloned this repository to your local machine with a terminal up and running
* Check that your Docker is running with the following command

`docker run hello-world`

# Running the Program

## Starting the Container
Type the command 

`sh docker-shell.sh` 

## Starting the dev API Server
Type the command inside the docker container prompt

`uvicorn_server` 


## Testing APIs
Go to `http://localhost:9500/` on your browser and you should see:

```
{"message":"Welcome to the API Service"}
```

Go to `http://localhost:9500/docs` on your browser and you should see the Swagger UI Documentation for the APIs




