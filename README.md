# 🚗 Car Price Estimator Web App

A machine learning web application built using **Flask**, **Pandas**, **Scikit-learn**, and **Bootstrap 5** to estimate the selling price of a used car based on input features like year, fuel type, brand, model, and more.

> ✅ Deployed on: [PythonAnywhere](https://your-pythonanywhere-link)  
> ✅ UI Inspired by: [SkyPrice Estimator](https://skyprice-estimator.onrender.com/)

---

## ✨ Features

- Predict car prices using a trained Linear Regression model
- Smart dropdowns for Brands & Models
- Clean, responsive, mobile-friendly UI with Bootstrap 5
- Real-time feedback via toast messages
- Live deployed web app using **PythonAnywhere**

---

## 🧠 Tech Stack

| Layer        | Tools & Libraries                                   |
|--------------|------------------------------------------------------|
| Frontend     | HTML5, CSS3, Bootstrap 5, JavaScript (vanilla)       |
| Backend      | Python, Flask                                        |
| ML Model     | Scikit-learn (Linear Regression), Pandas             |
| Deployment   | PythonAnywhere                                       |
| Data         | Cleaned version of [CarDekho used cars dataset](https://www.kaggle.com/datasets/snehaanbhadani/used-cars-price-prediction)

---



## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```


---
## FOLDER STRUCTURE

```bash
car-price-estimator/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation (for GitHub)
│
├── models/                    # ML-related files
│   ├── linear_model.pkl       # Trained regression model
│   ├── scaler.pkl             # Scaler for numeric features
│   ├── le_brand.pkl           # LabelEncoder for brands
│   └── le_model.pkl           # LabelEncoder for models
│
├── data/                      # Dataset(s)
│   └── CAR DETAILS FROM CAR DEKHO.csv
│
├── templates/                 # HTML templates (Flask Jinja2)
│   └── index.html             # Main frontend page
│
├── static/                    # Static assets (CSS, JS, images)
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   └── script.js          # (Optional) Custom JS
│   └── assets/
│       └── screenshots/       # Images used in README
│           ├── form.png
│           └── result.png
│
└── .gitignore                 # Ignore venv, __pycache__, etc.
```


