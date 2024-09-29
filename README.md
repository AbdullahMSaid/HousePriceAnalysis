# California House Price Analysis & Prediction

## Description
This project aims to predict housing prices in California using data features such as location, age, and socio-economic indicators. The analysis includes data preprocessing, feature engineering, and building a machine learning model using Random Forest regression.

## Table of Contents
- [Installation](#installation)
- [Project Overview](#project-overview)
- [Exploratory Data Analysis](#exploratory-data-analysis-eda)
- [Feature Engineering and Model Building](#feature-engineering-and-model-building)
- [Results and Evaluation](#results-and-evaluation)
- [Interactive Price Prediction App](#interactive-price-prediction-app)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [Contact Information](#contact-information)

## Installation
Clone this repository and install the required packages:

```bash
git clone https://github.com/AbdullahMSaid/HousePriceAnalysis.git
cd HousePriceAnalysis
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run price_predictor.py
```

 Open the URL displayed in the terminal to interact with the house price prediction app.

# Project Overview

The goal is to predict house prices based on a set of features including location, housing age, total rooms, and more.

## Dataset
- **Source**: California Housing Prices Dataset  
- **Size**: 20,000 samples  
- **Features**: 17 attributes such as `latitude`, `longitude`, `median_income`, etc.

## Exploratory Data Analysis (EDA)
During EDA, we visualized correlations and distributions of key variables. Example:

## Feature Engineering and Model Building
- **Model Used**: Random Forest Regressor  
- **Training RMSE**: 16,802.66  
- **Test RMSE**: 45,816.22  
- **Training R²**: 0.97  
- **Test R²**: 0.79  

## Results and Evaluation
The model performed well with a test R² of 0.79, indicating good predictive power.

## Interactive Price Prediction App
Use the Streamlit app to predict house prices by selecting various parameters:

## Future Work
- Hyperparameter tuning  
- Additional feature engineering  
- Experimenting with different ML models  

## Contributing
Feel free to submit issues and pull requests!

## Contact Information
- **GitHub**: [AbdullahiMSaid](https://github.com/AbdullahMSaid)  
- **LinkedIn**: [Abdullahi M Said](https://www.linkedin.com/in/abdullahi-m-said/)

