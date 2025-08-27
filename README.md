🏠 **House Price Prediction
******
This project implements a Machine Learning model to predict housing prices based on various features such as income, location, and population using the California Housing Dataset.
The goal is to build, train, and evaluate models to achieve accurate predictions of house prices.

📌 Features

Data preprocessing and cleaning
Exploratory Data Analysis (EDA) with visualizations
Feature scaling using StandardScaler
Model training with:
Linear Regression
Random Forest Regressor
Model evaluation using RMSE and R² Score
Comparison of model performances

📂 Dataset
The dataset used is the California Housing Dataset, which can be loaded directly from scikit-learn.
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

⚙️ Installation
Clone this repository and install the required dependencies:
git clone https://github.com/yourusername/HousePricePrediction.git
cd HousePricePrediction
pip install -r requirements.txt

🛠️ Requirements

Python 3.8+
numpy
pandas
matplotlib
seaborn
scikit-learn

Install them with:
pip install numpy pandas matplotlib seaborn scikit-learn

🚀 Usage
Run the script to train and evaluate the models:
python house_price_prediction.py

The script will:
Load and preprocess the dataset
Train Linear Regression and Random Forest models
Output RMSE and R² scores
Display visualizations for better un
