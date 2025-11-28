# 🚗 Car Price Prediction System  
### End-to-End Machine Learning Project with Tkinter UI

This project predicts the **selling price of used cars** using a trained machine learning model.  
It covers the complete ML pipeline from **data preprocessing → feature engineering → model training → deployment** through a clean and interactive **Tkinter desktop application**.

## 📚 Table of Contents
- Overview
- Features
- Workflow
- Project Structure
- Tech Stack
- Project Outcome

## ✨ Overview
This system analyzes multiple car-related features such as brand, model year, mileage, fuel type, and region to predict an accurate selling price.  
The model is trained using machine learning and deployed in a standalone **Tkinter GUI**, making it simple to use without Jupyter Notebook.

## 📌 Features

### 🔍 1. Data Preprocessing
- Handles missing values  
- One-Hot Encoding for categorical fields  
- Removes duplicates  
- Cleans inconsistent entries  
- Normalizes numerical features  

### ⚙️ 2. Feature Engineering
Key extracted features:
- Car brand  
- Vehicle type  
- Model year  
- Mileage  
- Fuel type  
- Transmission  
- Engine power  

Additional processing:
- Encoded **598+ columns** using sparse techniques  
- Selected optimal features for the model  

### 🤖 3. Model Training
- Trained using **Random Forest Regressor**  
- Dataset split into **Training** and **Testing** sets  
- Evaluated with:
  - **MSE**
  - **RMSE**
  - **MAE**  
- Final model saved as **car_price_model.pkl**

### 🖥️ 4. Tkinter Desktop App
User-friendly GUI for predicting car prices.

**Input Fields:**
- Brand  
- Model Year  
- Mileage  
- Fuel Type  
- Transmission  
- Region  

**Features:**
- Loads the trained .pkl model  
- Predicts price instantly  
- Lightweight & standalone  

## 🧠 Workflow
Raw Dataset 
     ↓
Preprocessing & Cleaning
     ↓
Feature Engineering
     ↓
One-Hot Encoding
     ↓
Random Forest Model Training
     ↓
Model Export (.pkl)
     ↓
Tkinter GUI Loads Model
     ↓
User Enters Car Details
     ↓
Predicted Car Price Displayed

## 📁 Project Structure
car-price-prediction/
│
├── dataset/
│   └── car_data.csv
│
├── model/
│   └── car_price_model.pkl
│
├── backend/
│   ├── model_training.py
│   └── preprocessing.py
│
├── ui/
│   └── app.py
│
└── README.md

## 🧪 Tech Stack
### Machine Learning
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  

### GUI (Frontend)
- Tkinter  

### Tools
- VS Code  
- Git & GitHub  

## 🎯 Project Outcome
- Gained experience in end-to-end ML workflows  
- Preprocessed large datasets efficiently  
- Trained and evaluated regression models  
- Built a complete ML-powered desktop application  
- Learned practical deployment using Tkinter  
