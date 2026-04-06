import streamlit as st
import joblib
import numpy as np

# --- Load model ---
model = joblib.load('salary_model.pkl')

intercept = model.intercept_
coefficient = model.coef_[0]

# --- Page config ---
st.set_page_config(
    page_title="Salary Intelligence Tool",
    page_icon="💼",
    layout="centered"
)

# --- Landing page ---
st.title("💼 Salary Intelligence Tool")
st.markdown("### Powered by Machine Learning")
st.markdown(
    "This tool uses a Linear Regression model trained on real salary data "
    "to help you understand the relationship between experience and salary."
)
st.markdown("---")

# --- Mode selection ---
st.subheader("What do you want to predict?")
mode = st.radio(
    label="Choose prediction direction:",
    options=[
        "I know my experience → Predict my salary",
        "I have a target salary → How many years do I need?"
    ]
)

st.markdown("---")

# --- Mode 1: Experience → Salary ---
if mode == "I know my experience → Predict my salary":
    st.subheader("🎯 Predict Your Salary")

    experience = st.slider(
        "Years of Experience",
        min_value=0.0,
        max_value=15.0,
        value=3.0,
        step=0.1
    )

    if st.button("Predict Salary"):
        prediction = intercept + coefficient * experience
        st.success(f"💰 Estimated Salary: **${prediction:,.2f}**")

        st.markdown("#### How this was calculated:")
        st.code(
            f"Salary = {intercept:,.2f} + ({coefficient:,.2f} × {experience})\n"
            f"Salary = ${prediction:,.2f}"
        )

# --- Mode 2: Salary → Experience ---
else:
    st.subheader("📈 How Much Experience Do You Need?")

    target_salary = st.number_input(
        "Enter your target salary ($)",
        min_value=20000,
        max_value=200000,
        value=80000,
        step=1000
    )

    if st.button("Calculate Experience Needed"):
        experience_needed = (target_salary - intercept) / coefficient

        if experience_needed < 0:
            st.warning(
                "That salary is below the base — even 0 years experience exceeds it.")
        else:
            st.success(
                f"📅 You need approximately **{experience_needed:.1f} years** "
                f"of experience to earn ${target_salary:,}"
            )

            st.markdown("#### How this was calculated:")
            st.code(
                f"Experience = (Target Salary - {intercept:,.2f}) / {coefficient:,.2f}\n"
                f"Experience = ({target_salary:,} - {intercept:,.2f}) / {coefficient:,.2f}\n"
                f"Experience = {experience_needed:.1f} years"
            )

# --- Footer ---
st.markdown("---")
st.caption(
    "Model: Linear Regression | R² = 0.90 | RMSE = $7,059 | "
    "Trained on 30 salary data points"
)
