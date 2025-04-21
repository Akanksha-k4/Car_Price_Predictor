from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
car = pd.read_csv('cleaned_quikr_car.csv')


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    car_data = {}
    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique())
        car_data[company] = models

    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_type, car_data=car_data)


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo-driven'))
    # print(company,car_model,year,fuel_type,kms_driven)

    input_df = pd.DataFrame([[company, car_model, year, fuel_type, kms_driven]], columns=[
                            'company', 'name', 'year', 'fuel_type', 'kms_driven'])
    prediction = model.predict(input_df)

    prediction_result = np.round(prediction[0], 2)

    return render_template('index.html',
                           companies=sorted(car['company'].unique()),
                           years=sorted(car['year'].unique(), reverse=True),
                           fuel_types=sorted(car['fuel_type'].unique()),
                           car_data={company: sorted(car[car['company'] == company]['name'].unique(
                           )) for company in car['company'].unique()},
                           prediction=prediction_result,
                           selected_company=company,
                           selected_model=car_model,
                           selected_year=year,
                           selected_fuel=fuel_type,
                           entered_kms=kms_driven)


if __name__ == '__main__':
    print("Flask app is running at http://127.0.0.1:5000/")
    app.run(debug=True)
