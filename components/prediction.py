import streamlit as st

def show_prediction():
    st.subheader("Make Predictions")
    st.write("Use trained models to make predictions.")
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
    st.write(f"Example input: Sepal Length = {sepal_length}")
