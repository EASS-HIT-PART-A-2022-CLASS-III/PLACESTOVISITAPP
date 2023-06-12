# places to visit
an app where u can add  update and delete cool places in the world.

Best Places to Visit API
This is a REST API built with FastAPI that provides information about the cool places to visit in various countries.

## HOW TO RUN THE BACKEND 
To run the backend in fastapi using Docker, you can use the following commands:


You can then build this image using the docker build command, specifying a tag name for the image:

`docker build -t my-fa -f./nginx.Dockerfile` after that 
`docker build -t my-fastapi-app` .
This assumes that your FastAPI application is in the current directory and that your dependencies are listed in a requirements.txt file in the same directory. You may need to modify the COPY and pip install commands if your application has different requirements or file locations.

Once the image is built, you can run it using the docker run command:


`docker run -p 8800:8800 my-fastapi-app`
This will start the FastAPI application in a container and map port 8800 on the container to port 8800 on the host machine. You can then access the application by navigating to http://localhost:8800/docs in a web browser or making requests to it programmatically.
