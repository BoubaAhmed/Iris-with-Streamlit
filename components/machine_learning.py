import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Path to the Iris dataset (assurez-vous que le chemin du fichier est correct)
default_dataset_path = "data/cleaned_dataset.csv"

def show_machine_learning():
    st.subheader("Modèles d'Apprentissage Automatique - Iris Dataset")
    st.write("Entraînez et évaluez des modèles de classification sur le jeu de données Iris.")

    # Charger le dataset
    df = pd.read_csv(default_dataset_path)
    
    # Assurez-vous que la colonne 'species' est bien catégorielle (labels discrets)
    if df['species'].dtype != 'object':
        df['species'] = df['species'].astype('category')  # Convertir en type catégoriel si nécessaire

    # Sélection du modèle
    model_name = st.selectbox("Choisissez un modèle", ["Régression Logistique", "Forêt Aléatoire", "SVM"])
    
    # Préparation des données
    target_column = 'species'  # La colonne cible pour Iris est 'species'
    X = df.drop(columns=[target_column])  # Caractéristiques (X)
    y = df[target_column]  # Variable cible (y)

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Normalisation des caractéristiques
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Entraînement et évaluation du modèle choisi
    if model_name == "Régression Logistique":
        model = LogisticRegression(max_iter=200)
    elif model_name == "Forêt Aléatoire":
        model = RandomForestClassifier(n_estimators=100)
    elif model_name == "SVM":
        model = SVC()

    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    
    # Affichage des résultats
    st.write(f"Précision du modèle : {accuracy_score(y_test, y_pred):.2f}")

