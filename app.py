from flask import Flask, render_template, request
import json
from collections import defaultdict
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and encoders once at startup
# with open("xgb_model.pkl", 'rb') as f:
#     model = pickle.load(f)    #its not working for deployment in cloud

with open("le_brand.pkl", 'rb') as f:
    le_brand = pickle.load(f)

with open("le_model.pkl", 'rb') as f:
    le_model = pickle.load(f)

with open('linear_model.pkl','rb') as f:
    model=pickle.load(f)

with open('scaler.pkl','rb') as f:
    scaler=pickle.load(f)

    

@app.route('/')
def index():
    brands = sorted(le_brand.classes_)
    
    # Create Brand → Model map
    df = pd.read_csv(r"C:\Users\prath\datasets\Internship_25_car_prediction_dataset\CAR DETAILS FROM CAR DEKHO.csv")
    df['name'] = df['name'].str.strip()
    df['Brand'] = df['name'].apply(lambda x: x.split()[0])
    df['Model'] = df['name'].apply(lambda x: ' '.join(x.split()[1:3]))
    top_100_models = df['Model'].value_counts().head(100).index
    df['Model'] = df['Model'].apply(lambda x: x if x in top_100_models else 'Other')

    brand_model_map = defaultdict(set)
    for brand, model in zip(df['Brand'], df['Model']):
        brand_model_map[brand].add(model)

    brand_model_map = {b: sorted(list(m)) for b, m in brand_model_map.items()}
    model_map_json = json.dumps(brand_model_map)

    return render_template('index.html', brands=brands, model_map=model_map_json)

   

@app.route('/predict', methods=['POST'])
def predict_price():
    # Get form data
    year = int(request.form.get('year'))
    km_driven = float(request.form.get('km_driven'))
    fuel = request.form.get('fuel').strip()
    transmission = request.form.get('transmission').strip()
    owner = request.form.get("owner").strip()
    Brand = request.form.get("Brand").strip()
    Model = request.form.get("Model").strip()

    # Preprocessing (same as training)
    fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4}
    transmission_map = {'Manual': 0, 'Automatic': 1}
    owner_map = {
        'First Owner': 0,
        'Second Owner': 1,
        'Third Owner': 3,
        'Fourth & Above Owner': 2,
        'Test Drive Car': 4
    }

    fuel_encoded = fuel_map.get(fuel, 0)
    transmission_encoded = transmission_map.get(transmission, 0)
    owner_encoded = owner_map.get(owner, 0)

    # Handle unknown brand/model safely
    try:
        brand_encoded = le_brand.transform([Brand])[0]
    except:
        brand_encoded = 0  # default or unknown

    try:
        # If not in top 100, use "Other"
        if Model not in le_model.classes_:
            Model = "Other"
        model_encoded = le_model.transform([Model])[0]
    except:
        model_encoded = 0

    # Create input DataFrame
    input_df = pd.DataFrame([{
        'year': year,
        'km_driven': km_driven,
        'fuel': fuel_encoded,
        'transmission': transmission_encoded,
        'owner': owner_encoded,
        'Brand': brand_encoded,
        'Model': model_encoded
    }])
    #Scaling
    input_df_scaled=scaler.transform(input_df)


    # Predict
    predicted_price = model.predict(input_df_scaled)[0]
    predicted_price = round(predicted_price)

    return f"<h2>Estimated Selling Price: ₹{predicted_price}</h2>"



if __name__ == '__main__':
    app.run(debug=True)
