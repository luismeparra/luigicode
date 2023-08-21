## luigicode Luis Mendez Parra  a01688471@tec.mx

## Airline Passenger Satisfaction

The present document is to enlist the final files that will be evaluated
and also add the link of everyone. 

### Deliverables Part 1


# Deliverable 1
README_Ent1.md In this file the reader can find the answers to the 3 questions made in the description from the task file. This file give a brief summary to understand the problem to solve , which solutions have been developed and which solution has the necesary to solve the classification problem.

Also has the baseline and the project scope of the project.

The link to acces the file is this :  [Title](README_Ent1.md)

# Deliverable 2

This file is a notebook that has the next sections to attend the business problem.

1. Setup: imports and configurations necessary to run the notebook from any machine.
2. Data load: instructions on how to download and/or load the data.
3. Data exploration: data analysis with statistical and visualization methods.
4. Data transformation: data cleaning, data transformation.
5. Model training: experimentation for model training.
6. Save model: save model.
7. Load and predict data: Load saved model and predict with new data.

The link to acces the file is this : `data-visualization-and-ml-for-psg-satisfaction.ipynb`:  Link: [Title](Notebooks/data-visualization-and-ml-for-psg-satisfaction.ipynb)


# Deliverable 3

This delivarable has two files:
 1. README.md file called README_VENV.md with the instructions to install a virtual enviroment in Windows and Linux. The link to acces the file is:  [Title](Deliverable_3/README_VENV.md)

 2. .txt file calle requirements.txt with the 
 package and vertions needed in the notebook of the deliverable 2. The link to acces the file is:  [Title](Deliverable_3/requirements.txt)



# Deliverable 4

This deliverable is the link of my GitHub repository with the content of all the deliverables from the project, the link is:

https://github.com/luismeparra/luigicode

# Deliverable 5

This deliverable is a Folder called tests with the unitary tests from the model trained in last steps. The link of the folder is :
[Title](tests)

Running tests, to run the test we can use testing framework like pytest to run your unit tests. Make sure you have pytest installed:

pip install pytest

Run the tests using the following command in your terminal while in the project directory:

pytest tests

This command will discover and run all the tests within the "tests" folder. Remember to replace your_module with the actual name of the Python module that contains your training data, custom transformers, and loaded model.

The  "tests" folder will contain these individual test files, and you can customize each test according to your project's structure and needs.

# Deliverable 6 

This deliverable is a .pre-commit-config.yamL file and you cand find here: 
[Title](.pre-commit-config.yaml)

Also if you don´t have installe pre-commit you can do this steps:

1.Run this command 
pip install pre-commit

2.Run the following command to set up the pre-commit hooks:

pre-commit install

With this configuration, when you commit your code, the pre-commit hooks will automatically format and lint your code according to the specified rules. If any of the checks fail, the commit will be rejected until the issues are resolved.

Please note that the exact versions of the tools (e.g., isort, black, autoflake, flake8) may change over time. You can find the latest versions and URLs for the repositories in the GitHub repositories of these tools.

Before proceeding, make sure to review the changes made by these tools to ensure that they align with your project's requirements and coding standards.

Also you can include conventional commits validation, the file that has this content is this: [Title](.pre-commit-config_conv_commits.yaml)

Instructions to use this file:

1.Add the above hooks configuration to your existing .pre-commit-config.yaml file.

2.Install the commitizen and cz-conventional-changelog packages if you haven't already:

pip install commitizen cz-conventional-changelog

3.Run the following command to set up the pre-commit hooks:

pre-commit install

With these hooks, your commit messages will be checked for conformance to the conventional commit format, ensuring that they have the required structure and adhere to the specified standards.

Please ensure that your commit messages follow the conventional commit format when making commits to your repository.

## Deliverable 7

This file has the next content:
1.Documented code (docstrings)
2.Annotations on functions 
3.Linting and formatting (This you can do it automatically with the pre-commit files:
-[Title](.pre-commit-config.yaml)
-[Title](.pre-commit-config_conv_commits.yaml)
)
4.Cookiecutter directory structure:
    -Creation of at least 6 Directories:
        >Classifier [Title](classifier)
        >Models [Title](models)
        >Preprocees [Title](preprocess)
        >load [Title](load)
        >train [Title](train)
        >data [Title](data)
And this files use Object-oriented programming
    -Modularization of code to be able to be instantiated from other scripts using classes.
    -Use of Custom Transformes.
    -Data pipeline that uses custom transformers.



## Deliverable 8

This file is a folder called api with the endpoints to train a model and predict a new value.

The link is here: [Title](api)

To Run the API 

1.Open a terminal.
2.Navigate to your project directory.
3.Run the following command to start the FastAPI server:

uvicorn api.app:app --reload

Now, your FastAPI application is running, and you can access it at http://127.0.0.1:8000.


Endpoints:

You can use tools like curl, Postman, or a Python script to interact with the API endpoints. For example, to train a new model, you can send a POST request to http://127.0.0.1:8000/train.

To make predictions, send a POST request to http://127.0.0.1:8000/predict with the input data in JSON format.

Remember to update paths, functions, and data loading to match your project's structure and requirements.



### Deliverables Part 2

# Deliverable 1
Logging.

All the modules were modified to add the logging with the purpose to get the lods. For example this : [Title](predict/predict.py)

Extra: A folder called utilities was created in the root  with a file called custom_logging.py with a class called CustomLogger. The link is this: [Title](utilities/custom_logging.py)


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

 # Deliverable 3