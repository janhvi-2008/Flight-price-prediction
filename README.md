# ✈️ Flight Price Prediction

A Machine Learning web application that predicts estimated flight ticket prices based on flight details.

## 🚀 Live Demo

👉 https://flight-price-prediction-jmm.streamlit.app/

# Flight Price Prediction ✈️

A Machine Learning project that predicts flight ticket prices using flight-related information such as airline, source, destination, departure time, class, duration, number of stops, and days left before departure.

## Project Overview

This project uses a **Random Forest Regression** model to predict flight prices. The dataset contains 500 flight records, and the `Price` column is used as the target variable.

Categorical features are converted using **One-Hot Encoding**, while numerical features are passed directly to the model through a Scikit-learn preprocessing pipeline.

## Features Used

* Airline
* Source
* Destination
* Departure Time
* Class
* Duration Hours
* Total Stops
* Days Left

## Machine Learning Model

**Random Forest Regressor**

* Number of estimators: 200
* Random state: 42
* Test size: 20%

## Model Performance

* **MAE:** 625.23
* **RMSE:** 783.04
* **R² Score:** 0.9275

The model achieved an R² score of approximately **92.75%** on the test dataset.

## Technologies Used

* Python 3.10
* Pandas
* NumPy
* Scikit-learn
* Random Forest Regression
* Jupyter Notebook
* Pickle

## Project Files

* `flight_data_500.csv` — Dataset used for training and testing
* `flight_price_model.pkl` — Trained Machine Learning model
* `flight_price_prediction.ipynb` — Jupyter Notebook containing the complete model development process

## How to Run

Install the required libraries:

```bash
pip install pandas numpy scikit-learn jupyter
```

Open the Jupyter Notebook:

```bash
jupyter notebook
```

Then open the project notebook and run the cells.

## Objective

The objective of this project is to develop a Machine Learning model that can estimate flight ticket prices based on available flight and travel information.

## Author

**Janhavi**

