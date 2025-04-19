import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model components
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="AI for Daily Budget Planner for Orphanage Resources Management", layout="centered")

# Always put a header or title first!
st.title("🤖 AI for Daily Budget Planner for Orphanage Resources Management")
st.markdown("Enter the shelter data to predict the suggested purchase item and quantity to buy.")

# Add custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)

# Form Inputs
with st.form("predict_form"):
    st.subheader("🔢 Input Shelter Data")

    col1, col2 = st.columns(2)
    with col1:
        num_children = st.number_input("Number of Children", min_value=0)
        food_remaining = st.number_input("Food Remaining (kg)", min_value=0.0)
        daily_need = st.number_input("Daily Food Need (kg)", min_value=0.0)
        food_used = st.number_input("Food Used Today (kg)", min_value=0.0)
        donation_amount = st.number_input("Donation Amount", min_value=0.0)

    with col2:
        expense_total = st.number_input("Total Expenses", min_value=0.0)
        budget_left = st.number_input("Budget Left", min_value=0.0)
        medical_cost = st.number_input("Medical Cost", min_value=0.0)
        utility_cost = st.number_input("Utility Cost", min_value=0.0)
        staff_on_duty = st.number_input("Staff On Duty", min_value=0)

    submitted = st.form_submit_button("🚀 Predict")

if submitted:
    epsilon = 1e-6
    food_per_child = food_used / (num_children + 1)
    donation_per_child = donation_amount / (num_children + 1)
    budget_per_child = budget_left / (num_children + 1)
    food_donation_ratio = food_used / (donation_amount + epsilon)
    budget_food_ratio = budget_left / (food_used + epsilon)

    # Prepare input data for prediction
    input_data = pd.DataFrame([{
        "Num_Children": num_children,
        "Food_Remaining": food_remaining,
        "Daily_Need": daily_need,
        "Food_Used": food_used,
        "Donation_Amount": donation_amount,
        "Expense_Total": expense_total,
        "Budget_Left": budget_left,
        "Medical_Cost": medical_cost,
        "Utility_Cost": utility_cost,
        "Staff_On_Duty": staff_on_duty,
        "Food_Per_Child": food_per_child,
        "Donation_Per_Child": donation_per_child,
        "Budget_Per_Child": budget_per_child,
        "Food_Donation_Ratio": food_donation_ratio,
        "Budget_Food_Ratio": budget_food_ratio
    }])

    # Scale the input data using the same scaler as the model
    input_scaled = scaler.transform(input_data)

    # Predict using the model (this should return the item to buy)
    prediction = model.predict(input_scaled)

    # Check if the model prediction returns a single value (item to buy)
    predicted_label = label_encoder.inverse_transform([prediction[0]])[0]  # Item to buy
    
    # Display the result (without trying to access index 1)
    st.success(f"🎯 **Suggested Purchase**: {predicted_label}")
    
    # Assuming that the model doesn't predict quantity separately,
    # we can estimate the quantity to buy (if necessary)
    estimated_quantity_to_buy = food_used * 2  # Example placeholder formula

    st.write(f"📦 **Estimated Quantity to Buy**: {estimated_quantity_to_buy} kg")
