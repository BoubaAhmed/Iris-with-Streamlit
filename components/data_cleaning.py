import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def show_data_cleaning():
    if 'df' not in st.session_state:
        st.warning("Please load a dataset first from the Dataset section.")
        return
    
    df = st.session_state.df
    st.subheader("Nettoyage et Prétraitement des Données")
    st.write("Cette étape consiste à nettoyer et préparer les données avant de les utiliser pour l'analyse et la modélisation.")
    
    # Convertir les noms de colonnes en chaînes de caractères (important pour éviter l'erreur)
    df.columns = df.columns.astype(str)

    # Affichage des premières lignes des données
    st.write("Voici les premières lignes du dataset :")
    st.dataframe(df.head())
    
    # 1. Gestion des valeurs manquantes
    st.write("### 1. Gestion des Valeurs Manquantes")
    if st.checkbox("Gérer les Valeurs Manquantes", value=True):
        # Choisir une méthode pour imputer les valeurs manquantes
        imputer_method = st.selectbox("Sélectionnez la méthode d'imputation", ["Moyenne", "Médiane", "Suppression"])
        
        if imputer_method == "Moyenne":
            imputer = SimpleImputer(strategy="mean")
        elif imputer_method == "Médiane":
            imputer = SimpleImputer(strategy="median")
        elif imputer_method == "Suppression":
            df = df.dropna()  # Supprimer les lignes avec des valeurs manquantes
            st.write("Les lignes avec des valeurs manquantes ont été supprimées.")
        
        if imputer_method != "Suppression":
            # Appliquer l'imputation sur les colonnes numériques
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            df[numeric_columns] = imputer.fit_transform(df[numeric_columns])  # Appliquer l'imputation
            st.write("Les valeurs manquantes ont été imputées avec la méthode choisie.")
        
        st.dataframe(df.head())
    
    # 2. Encodage des données catégorielles
    st.write("### 2. Encodage des Données Catégorielles")
    if st.checkbox("Encoder les Données Catégorielles", value=True):
        categorical_columns = df.select_dtypes(include=['object']).columns  # Identifier les colonnes catégorielles
        
        # Utiliser LabelEncoder pour transformer les variables catégorielles en numériques
        label_encoder = LabelEncoder()
        for col in categorical_columns:
            df[col] = label_encoder.fit_transform(df[col])
            st.write(f"La colonne `{col}` a été encodée.")
        
        st.dataframe(df.head())
    
    # 3. Mise à l'échelle des caractéristiques numériques
    st.write("### 3. Mise à l'échelle des Caractéristiques Numériques")
    if st.checkbox("Mettre à l'échelle les Caractéristiques Numériques", value=True):
        # Identifier les colonnes numériques
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        
        # Standardisation des données : mise à l'échelle des caractéristiques
        scaler = StandardScaler()
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
        
        st.write("Les caractéristiques numériques ont été mises à l'échelle.")
        
        st.dataframe(df.head())

    # Option de sauvegarde des données nettoyées
    if st.button("Sauvegarder le Dataset Nettoyé"):
        cleaned_dataset_path = "data/cleaned_dataset.csv"
        df.to_csv(cleaned_dataset_path, index=False)
        st.write(f"Les données nettoyées ont été sauvegardées sous : `{cleaned_dataset_path}`")
