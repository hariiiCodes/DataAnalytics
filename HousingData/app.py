import streamlit as st
import pandas as pd
import joblib

model = joblib.load("americanHousingModel.pkl")

st.title("🏠 American Housing Price Prediction")
st.write("Enter the details below to predict the house price.")

index = st.number_input("Index", value=1)
zip_code = st.number_input("Zip Code", value=10013)
beds = st.number_input("Beds", value=2)
baths = st.number_input("Baths", value=2)
living_space = st.number_input("Living Space", value=1000)

city = st.number_input("Encoded City", value=0)
state = st.number_input("Encoded State", value=0)

zip_population = st.number_input("Zip Code Population", value=20000)
zip_density = st.number_input("Zip Code Density", value=5000)

county = st.number_input("Encoded County", value=0)

income = st.number_input("Median Household Income", value=50000)

latitude = st.number_input("Latitude", value=40.0)
longitude = st.number_input("Longitude", value=-74.0)

if st.button("Predict House Price"):

    input_data = pd.DataFrame([[
        index,
        zip_code,
        beds,
        baths,
        living_space,
        city,
        state,
        zip_population,
        zip_density,
        county,
        income,
        latitude,
        longitude
    ]], columns=[
        'index',
        'Zip Code',
        'Beds',
        'Baths',
        'Living Space',
        'City',
        'State',
        'Zip Code Population',
        'Zip Code Density',
        'County',
        'Median Household Income',
        'Latitude',
        'Longitude'
    ])

    prediction = model.predict(input_data)

    st.success(f"Predicted Price: ${prediction[0]:,.2f}")