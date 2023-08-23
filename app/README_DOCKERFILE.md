# Deliverable 2

Docker 

A file called Dockerfile was created in the root directory and these are the instructions to build the image, execute the container, debug the container, make predictions and copy the logs. 

-Build an Image:

You can build an image using the following command in the terminal , be sure you are in the project´s root directory. 

docker build -t api-image .

-Run the container: 

To run the container from the built image you need to use the next command:

docker run -d -p 8000:8000 --name api-container api-image

This command will start the cointainer in dtached mode with the name api-container, to acces the API running inside the container, it is posible to make requests to http://localhost:8000

-Debug a container:

Use this command to acces a shell inside the running container.

docker exec -it api-container bash

With this command it will open a bash inside the container to run commandas and debug the API.

-Predictions:

It is possible too send requests to the api RUNNING container with this command example:

curl -X POST -H "Content-Type: application/json" -d '{"gender": "female", "age": 30}' http://localhost:8000/predict

-Copy Logs:

With the following command it is possible copy the logs from the container to the logs directory on local machine.

docker cp api-container:/app/app.log ./logs/
