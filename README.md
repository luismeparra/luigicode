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

* 1. [Title](Docs/data-visualization-and-ml-for-psg-satisfaction.ipynb)
* 2. [Title](Docs/airline-passenger-satisfaction-eda-ml.ipynb)
* 3. [Title](Docs/passengerssatisfaction-outlierdetection-97-recall.ipynb)

## Setup

### Python version and packages to install

Note: Change the directoy to the root folerd.

We need to create a virtual environment with Python 3.10.

    ```bash
    python -m venv venv
    ```

After that we need to activate with the following command:

    ```bash
   venv\Scripts\activate
   ```

After we need to install libraries we neeed to run the following command to install the libraries/packages.

    ```bash
    pip install -r requirements.txt  
    ```
[Title](requirements.txt)

## Model training from a main file

To train the Random Forest Model, only run the following code:

```bash
python luigicode/main.py
```

The link of the file is this: [Title](main.py) 

The model was saved in  ./models/random_forest_output.pkl

## Execution of unit tests

