# luigicode Luis Méndez Parra  a01688471@tec.mx

# Airline Passenger Satisfaction

## Table of Contents 
- [Problem Statement](#problem-statement)
- [Developed Notebooks](#developed-notebooks)
- [Best Solution](#best-solution)
- [Potential Models](#potential-models)
- [Future Work](#future-work)

## 1 Problem Statement 

Which problem aboard?

The project is about to try to predict the satisfaction level ((Satisfaction, neutral or dissatisfaction)) 
for  a passenger that has had a flight in the airline using several features like: 

Gender: Gender of the passengers (Female, Male)

Customer Type: The customer type (Loyal customer, disloyal customer)

Age: The actual age of the passengers

Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)

Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus)

Flight distance: The flight distance of this journey

Inflight wifi service: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)

Departure/Arrival time convenient: Satisfaction level of Departure/Arrival time convenient

Ease of Online booking: Satisfaction level of online booking

Gate location: Satisfaction level of Gate location

Food and drink: Satisfaction level of Food and drink 

and others ...

## 2 Developed Solutions in Notebooks found in Kaggle

The most accesible notebooks that give a solution that allows to facilitate interactive data analysis and model development are the next:

Includes all the preprocessing steps like data cleaning, handling missing values, outlier detection,exploratory data analysis and contains different Machine Learning models, their training and evaluation process. These notebooks help us to decide the best performing model.

- `airline-passenger-satisfaction-eda-ml.ipynb`:  Link: [Title](Notebooks/airline-passenger-satisfaction-eda-ml.ipynb)

- `data-visualization-and-ml-for-psg-satisfaction.ipynb`:  Link: [Title](Notebooks/data-visualization-and-ml-for-psg-satisfaction.ipynb)


## 3 Which of all solutions has the necesary to train and save the model?

The solution `data-visualization-and-ml-for-psg-satisfaction.ipynb` presents a RandomForestClassifier model provides the best results in our comparison of models in terms of AUROC metric. This model was trained using the training set and saved for future predictions.


## Potential Models : 'Which models can be used to develop a model beyond the solution given in Kaggle?'

Several other models could have been used to solve this problem:

- Decision Trees: A straightforward model that is easy to interpret. It could have provided good results if the relationship between variables
   was non-linear and hierarchical.

- Support Vector Machines: Can offer good results when the boundary between satisfaction and non-satisfaction is not linear.

- Neural Networks: If the dataset was significantly larger, shallow neural networks or deep learning models could potentially improve results.

- Gradient Boosting Machines, like XGBoost or LightGBM, could be used to potentially achieve better results.

## Project Scope

The project has the purpose to attend the problem of get the satisfaction level of a customer from an airline through analytical solutions like ML models. Once the model has been developed the final step is to construct an API REST to consume the model without expose the source code of the model.
  
## Future Work
> Any plans for future enhancements or model improvements.

Going forward, better preprocessing or feature engineering could improve the model's performance. We could also try ensemble methods or sophisticated models like Neural Networks. Additionally, we could use techniques like boost and bagging to improve the model's accuracy.

