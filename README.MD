# 🚗 Car Price Prediction Using Machine Learning
### *A complete pipeline: Data → Preprocessing → Feature Engineering → Model Training → Deployment (Tkinter UI)*

## 📌 Project Overview
This project predicts the **selling price of used cars** using machine learning.  
It covers the complete lifecycle of an ML project — from importing raw data to delivering a user-friendly desktop application.

The model is trained on a dataset containing **188,534 rows** and **598 columns**, including attributes like:

- Car brand  
- Model year  
- Mileage  
- Transmission type  
- Fuel type  
- Owner category  
- Engine power  
- Torque  
- Seating capacity  
- Price (target)

The final model is deployed using a **Tkinter GUI**, where the user enters car details and instantly receives the **predicted price**.

## 🧠 Features
- Complete data preprocessing pipeline  
- Feature engineering with OHE & scaling  
- Training using **Random Forest Regressor**  
- Model evaluation using MSE, RMSE, and MAE  
- Saving model using `pickle`  
- Desktop app built with **Tkinter**  
- Clean UI for entering car specifications  
- Instant price prediction  

## 🗂️ Project Architecture
Raw Dataset → Cleaning → Feature Engineering → OHE → Model Training → Model Saving → Tkinter UI → Prediction

## ⚙️ Tech Stack
- **Python**
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  
- Tkinter  

## 📊 Model Performance
| Metric | Score |
|--------|--------|
| **MSE** | 50,531,292,284 |
| **RMSE** | 224,791 |
| **MAE** | 102,242 |

## 🧱 Folder Structure
```
Project  
│── data/  
│── models/  
│── car_price_model.py  
│── app.py  
│── requirements.txt  
│── README.md  
```

## 🎯 Conclusion
A complete end-to-end ML project demonstrating dataset cleaning, ML modeling, and model deployment using Tkinter.
