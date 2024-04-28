import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    data = pd.read_csv('FastFoodNutritionMenuV3.csv')
    return data

data = load_data()

def get_nutritional_values(dish_name):
    dish_info = data[data['Item'] == dish_name]

    if dish_info.empty:
        return "Dish not found in the dataset"

    # Extracting nutritional values
    calories = dish_info['Calories'].values[0]
    total_fat = dish_info['Total Fat\n(g)'].values[0]
    saturated_fat = dish_info['Saturated Fat\n(g)'].values[0]
    cholesterol = dish_info['Cholesterol\n(mg)'].values[0]
    sodium = dish_info['Sodium \n(mg)'].values[0]
    carbs = dish_info['Carbs\n(g)'].values[0]
    fiber = dish_info['Fiber\n(g)'].values[0]
    sugars = dish_info['Sugars\n(g)'].values[0]
    protein = dish_info['Protein\n(g)'].values[0]

    # Constructing the response
    response = f"Nutritional values for {dish_name}:\n"
    response += f"Calories: {calories}\n"
    response += f"Total Fat: {total_fat}g\n"
    response += f"Saturated Fat: {saturated_fat}g\n"
    response += f"Cholesterol: {cholesterol}mg\n"
    response += f"Sodium: {sodium}mg\n"
    response += f"Carbs: {carbs}g\n"
    response += f"Fiber: {fiber}g\n"
    response += f"Sugars: {sugars}g\n"
    response += f"Protein: {protein}g\n"

    return response

# Streamlit interface
st.title('Nutritional Information Finder')

dish_input = st.text_input('Enter the name of the dish to get its nutritional values:', '')

if st.button('Get Nutritional Values'):
    result = get_nutritional_values(dish_input)
    st.text(result)
