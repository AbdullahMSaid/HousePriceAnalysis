import streamlit as st
import joblib
import pandas as pd

# Load the saved model and feature names
model_data = joblib.load('house_forest_model_with_features.pkl')
model = model_data['model']
feature_names = model_data['feature_names']

# Define California cities with their latitude and longitude
cities = {
    "Los Angeles": {"latitude": 34.0522, "longitude": -118.2437, "location_type": {"<1H OCEAN": 0, "INLAND": 1, "ISLAND": 0, "NEAR BAY": 0, "NEAR OCEAN": 0}},
    "San Francisco": {"latitude": 37.7749, "longitude": -122.4194, "location_type": {"<1H OCEAN": 1, "INLAND": 0, "ISLAND": 0, "NEAR BAY": 1, "NEAR OCEAN": 1}},
    "San Diego": {"latitude": 32.7157, "longitude": -117.1611, "location_type": {"<1H OCEAN": 1, "INLAND": 0, "ISLAND": 0, "NEAR BAY": 1, "NEAR OCEAN": 1}},
    "Sacramento": {"latitude": 38.5816, "longitude": -121.4944, "location_type": {"<1H OCEAN": 0, "INLAND": 1, "ISLAND": 0, "NEAR BAY": 0, "NEAR OCEAN": 0}},
    "Fresno": {"latitude": 36.7378, "longitude": -119.7871, "location_type": {"<1H OCEAN": 0, "INLAND": 1, "ISLAND": 0, "NEAR BAY": 0, "NEAR OCEAN": 0}},
    "Santa Barbara": {"latitude": 34.4208, "longitude": -119.6982, "location_type": {"<1H OCEAN": 1, "INLAND": 0, "ISLAND": 0, "NEAR BAY": 0, "NEAR OCEAN": 0}},
    "Santa Catalina Island": {"latitude": 33.3871, "longitude": -118.4220, "location_type": {"<1H OCEAN": 0, "INLAND": 0, "ISLAND": 1, "NEAR BAY": 0, "NEAR OCEAN": 0}}  # Added island location
}

# Streamlit app title
st.title("House Price Predictor")

# Step 1: User selects a city
st.header("Select a California City")
selected_city = st.selectbox("Choose a city", list(cities.keys()))

# Get the corresponding latitude, longitude, and location type
latitude = cities[selected_city]["latitude"]
longitude = cities[selected_city]["longitude"]
location_type = cities[selected_city]["location_type"]

# Display the selected city coordinates and geographic status
st.write(f"Selected City: {selected_city}")
st.write(f"Latitude: {latitude}, Longitude: {longitude}")
st.write(f"Geographic Status: {' | '.join([key for key, value in location_type.items() if value == 1])}")  # Displaying geographic status

# Step 2: Input selectors for other features
housing_median_age = st.slider("Housing Median Age (0-60)", 0, 60, 30)
total_rooms = st.slider("Total Rooms (0-10)", 0, 10, 5)
total_bedrooms = st.slider("Total Bedrooms (0-10)", 0, 10, 5)
population = st.slider("Population (0-10)", 0, 10, 5)
households = st.slider("Households (0-8)", 0, 8, 4)
median_income = st.slider("Median Income (0.0-15.0)", 0.0, 15.0, 7.5)
rooms_per_household = st.slider("Rooms per Household (0-5)", 0.0, 5.0, 2.5)
population_per_household = st.slider("Population per Household (0-5)", 0.0, 5.0, 2.5)
bedrooms_per_room = st.slider("Bedrooms per Room (0-5)", 0.0, 5.0, 2.5)

# Step 3: Toggle for is_high_population_density
is_high_population_density = st.selectbox("Is High Population Density?", [0, 1])

# Step 4: Prepare the input data for prediction
input_data = {
    "latitude": latitude,
    "longitude": longitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    "rooms_per_household": rooms_per_household,
    "population_per_household": population_per_household,
    "bedrooms_per_room": bedrooms_per_room,
    **location_type,  # Unpack location type features
    "is_high_population_density": is_high_population_density  # Include the toggle
}

# Create a DataFrame using the defined order of feature names
input_df = pd.DataFrame([input_data])[feature_names]

# Step 5: Button to predict price
if st.button("Predict Price"):
    predicted_price = model.predict(input_df)
    st.write(f"Estimated House Price: ${predicted_price[0]:,.2f}")
