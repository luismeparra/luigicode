# ITESM MLOPS Project - Luis Méndez Parra A01688471

# PASSENGER SATISFACTION PREDICTION MODEL

## Introduction

This is the final project, where we delve into the core aspects of ML frameworks and their real-world application. Throughout this undertaking, we'll put into practice fundamental tools and concepts essential for crafting software within the MLOps realm. This journey encompasses not only environment setup but also optimal practices for conceiving ML models and deploying them.

## About the project

Our mission with this project is to architect a sturdy and reproducible MLOps workflow for the development, training, and deployment of machine learning models. We'll begin with a random forest model as a proof of concept due to its straightforward nature. This model will be applied to the Airline Passenger Satisfaction dataset ( https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction ) to predict the level satisfaction of a passenger's airline based on specific attributes.

The project encompasses the following key areas:

1. **Key concepts of ML systems**  
In this segment, we lay the foundation for MLOps by providing insights into the lifecycle and architecture of ML systems.

2. **Basic concepts and tools for software development**  
This module is dedicated to introducing the fundamental principles of software development that serve as the base of MLOps.

3. **Development of ML models**  
Here, we see the creation of an ML model. Starting from experimentation in notebooks, we delve into code refinement and ultimately culminate in the creation of an API to serve the model.

4. **Deployment of ML models**  
The objective of this module is to show how a model is served as a web service to make predictions.

5. **Integration of concepts**  
The final module is a fusion of all the wisdom gathered in previous sections. Witness the integration in action as we present a demonstration of Continuous Delivery in practice.

### Baseline

Lead the orchestration of a comprehensive workflow. This encompasses everything from honing data to unveiling a local web service, all centered around harnessing the predictive prowess of a supervised model. Our info is the Satisfaction Passanger Airline dataset, and we try to get insights into the passengers' satisfaction during his journey on the airline.

### Scope 

The project has the purpose to attend the problem of get the satisfaction level of a customer from an airline through analytical solutions like ML models. Once the model has been developed the final step is to construct an API REST to consume the model without expose the source code of the model.

Note:This project is planned to cover the topics seen in the course syllabus, which was designed to include technical capacity levels 0, 1 and a small part of 2 of [Machine Learning operations maturity model - Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model).


### Links to experiment in notebooks

You can try to explore this notebooks to find different analytics solutions.

* 1. [data-visualization-and-ml-for-psg-satisfaction](Docs/data-visualization-and-ml-for-psg-satisfaction.ipynb)
* 2. [airline-passenger-satisfaction-eda-ml](Docs/airline-passenger-satisfaction-eda-ml.ipynb)
* 3. [passengerssatisfaction-outlierdetection-97-recall](Docs/passengerssatisfaction-outlierdetection-97-recall.ipynb)

## Setup

Firstable is importante to change the name luis.mendez defined in the path :
"C:\Users\luis.mendez\luigicode\..." to the user name of your local computer in the tests.py file and app.py file.

### Python version and packages to install

Note: Change the directoy to the root folerd.

We need to create a virtual environment with Python 3.10.

    ```
    python -m venv venv
    ```

After that we need to activate with the following command:

    ```
    venv\Scripts\activate
    ```

After we need to install libraries we neeed to run the following command to install the libraries/packages.

    ```
    pip install -r requirements.txt  
    ```

[requirements](requirements.txt)

## Model training from a main file

To train the Random Forest Model, only run the following code:

```
python luigicode/main.py
```

The link of the file is this: [main.py](main.py) 

The model was saved in  ./models/random_forest_output.pkl

## Execution of unit tests

You can find a folder called tests in the root directory where the following tests have been defined:
[Tests folder](tests)

* Test `test_missing_indicator_transform`:  
Test the `transform` method of the MissingIndicator transformer.

* Test `test_missing_indicator_fit`:  
Test the `fit` method of the MissingIndicator transformer.

* Test `test_csv_file_existence`:  
Test case to check if the CSV file exists.

* Test `test_model_existence`:  
Test to validate the existence of a `.pkl` model file.


### Execution instructions

Test to try Data Retriever Class defined in the load folder in load_data.py

The following test validates the [load_data.py](itesm_mlops_project/load/load_data.py) module, with the `DataRetriever` class.

Follow the next steps to run the test.

* Run in the terminal:

    ```bash
    pytest ./tests/tests.py::test_csv_file_existence -v
    ```

* You should see the following data output:


    ```pytest
    ================================================= test session starts =================================================
platform win32 -- Python 3.10.9, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\luis.mendez\luigicode\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\luis.mendez\luigicode
plugins: anyio-3.7.1
collected 1 item

tests/tests.py::test_csv_file_existence PASSED                                                                   [100%]

================================================= 1 passed in 10.38s ==================================================
    ```


And Also you can try all the test with the same procedure only you need to change the name of the test you want to try in the command:


    ```
    pytest ./tests/tests.py::name_of_tests -v
    ```

The tests are: test_missing_indicator_transform , test_missing_indicator_fit, test_model_existence

## Usage 

### Individual Fastapi and Use Deployment

To display the API we need to run the next command:

uvicorn api.app:app --reload


    ```
    uvicorn api.app:app --reload
    ```
#### Checking endpoints

To check the endpoints we need to:

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Titanic is all ready to go!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:

