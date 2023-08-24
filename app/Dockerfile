# Use a base Python image
FROM python:3.11-slim
# Set the working directory inside the container
WORKDIR /app
#WORKDIR C:/Users/luis.mendez/luigicode/app
# Copy the files to the working directory
COPY . .
COPY app.py .
COPY requirements.txt .
COPY ml_models/random_forest_model_output.pkl 


# Install the project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt 
#RUN apt-get update && apt-get install -y vim 

# Expose the port of your API

EXPOSE 8000


# Run the API when the container is started
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]


#uvicorn api.app:app --reload
