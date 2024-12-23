import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_eda():
    st.subheader("Exploratory Data Analysis (EDA)")

    # Ensure that the dataset is available for EDA
    if 'df' not in st.session_state:
        st.warning("Please load a dataset first from the Dataset section.")
        return
    
    df = st.session_state.df  # Retrieve the dataset from session state

    # Display basic info about the dataset
    st.write("### Basic Information")
    st.write("**Number of Rows and Columns:**", df.shape)
    st.write("**Data Types:**", df.dtypes)
    st.write("**Missing Values:**")
    st.dataframe(df.isnull().sum())
    
    # Show dataset summary statistics
    st.write("### Dataset Summary Statistics")
    st.dataframe(df.describe())

    # Visualizing missing data (if any)
    st.write("### Missing Data Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))  # Create figure and axis objects
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)  # Pass the axis to the heatmap
    st.pyplot(fig)  # Now we pass the figure object explicitly to st.pyplot()

    # Visualizing distributions of numerical features
    st.write("### Distribution of Numerical Features")
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        st.write(f"#### {col} Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

    # Visualizing pairwise relationships between numerical features
    st.write("### Pairplot of Numerical Features")
    if len(num_cols) > 1:
        fig = sns.pairplot(df[num_cols])
        st.pyplot(fig)

    # Visualizing correlations between numerical features
    st.write("### Correlation Heatmap")
    correlation_matrix = df[num_cols].corr()  # Only compute correlation for numerical columns
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)

    # Visualizing relationships between categorical and numerical features
    st.write("### Boxplots for Categorical vs Numerical Features")
    cat_cols = df.select_dtypes(include=['object']).columns
    for cat_col in cat_cols:
        for num_col in num_cols:
            st.write(f"#### {cat_col} vs {num_col}")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x=df[cat_col], y=df[num_col], ax=ax)
            st.pyplot(fig)

    # Visualizing categorical feature distribution
    st.write("### Distribution of Categorical Features")
    for cat_col in cat_cols:
        st.write(f"#### {cat_col} Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data=df, x=cat_col, ax=ax)
        st.pyplot(fig)

    # Visualizing outliers using boxplots (for numerical features)
    st.write("### Outliers Detection (Boxplots)")
    for col in num_cols:
        st.write(f"#### {col} Outliers")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(df[col], ax=ax)
        st.pyplot(fig)

    st.write("### EDA Complete")
    st.write("Now that we have explored the data, it's time to move on to the next steps in the analysis!")
