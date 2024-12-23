import streamlit as st

def show_machine_learning():
    st.subheader("Machine Learning Models")
    st.write("Train and evaluate ML models here.")
    st.selectbox("Choose Model", ["Logistic Regression", "Random Forest", "SVM"])
