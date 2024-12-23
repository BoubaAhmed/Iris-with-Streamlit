import streamlit as st
from components import about, dataset, eda, data_cleaning, machine_learning, prediction, conclusion


st.set_page_config(layout="wide")

# Function to handle page selection
def set_page_selection(page):
    st.session_state.page_selection = page

# Ensure session state is initialized
if "page_selection" not in st.session_state:
    st.session_state.page_selection = "about"

# Sidebar with active button logic
with st.sidebar:
    st.sidebar.markdown("### 📂 Navigation")
    
    # Navigation Buttons with Active Button Logic
    if st.sidebar.button("📖 About", use_container_width=True): 
        set_page_selection("about")
    if st.sidebar.button("📊 Dataset", use_container_width=True):
        set_page_selection("dataset")
    if st.sidebar.button("📈 EDA", use_container_width=True):
        set_page_selection("eda")
    if st.sidebar.button("🧹 Data Cleaning", use_container_width=True):
        set_page_selection("data_cleaning")
    if st.sidebar.button("🤖 Machine Learning", use_container_width=True):
        set_page_selection("machine_learning")
    if st.sidebar.button("🔍 Prediction", use_container_width=True):
        set_page_selection("prediction")
    if st.sidebar.button("📜 Conclusion", use_container_width=True):
        set_page_selection("conclusion")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("📌 **Tip:** Navigate through the sections above to explore the full ML workflow.")

# Main Content Logic (Displays content based on the selected page)
if st.session_state.page_selection == "about":
    about.show_about()
elif st.session_state.page_selection == "dataset":
    dataset.show_dataset()
elif st.session_state.page_selection == "eda":
    eda.show_eda()
elif st.session_state.page_selection == "data_cleaning":
    data_cleaning.show_data_cleaning()
elif st.session_state.page_selection == "machine_learning":
    machine_learning.show_machine_learning()
elif st.session_state.page_selection == "prediction":
    prediction.show_prediction()
elif st.session_state.page_selection == "conclusion":
    conclusion.show_conclusion()
