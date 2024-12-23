import streamlit as st
import pandas as pd
import os

def show_dataset():
    st.subheader("Dataset Overview")

    # Set the path to the default dataset
    default_dataset_path = "data/iris.csv"

    # Check if the default dataset exists
    if os.path.exists(default_dataset_path):
        st.write("### Default Dataset Loaded")
        df_default = pd.read_csv(default_dataset_path)
        st.write("Preview of the Default Dataset:")
        st.dataframe(df_default.head())
        
        # Show basic info and statistics of the default dataset
        st.write("### Default Dataset Summary")
        st.write(f"**Number of Rows:** {df_default.shape[0]}")
        st.write(f"**Number of Columns:** {df_default.shape[1]}")
        st.write("### Dataset Statistics")
        st.dataframe(df_default.describe())
        
        st.session_state.df = df_default
    else:
        st.write("### No default dataset found in the `/data` folder.")
    
    # Allow the user to upload a custom dataset
    uploaded_file = st.file_uploader("Upload your own dataset", type=["csv", "xlsx"])

    if uploaded_file:
        # Check file type
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)

        st.write("Dataset successfully uploaded!")
        st.write("Preview of your uploaded dataset:")
        st.dataframe(df.head())
        
        # Display summary of the uploaded dataset
        st.write("### Dataset Summary")
        st.write(f"**Number of Rows:** {df.shape[0]}")
        st.write(f"**Number of Columns:** {df.shape[1]}")
        st.write("### Dataset Statistics")
        st.dataframe(df.describe())
