import streamlit as st

def show_about():

    # Titre et présentation du projet
    st.title("À propos de ce projet de Machine Learning")
    
    st.markdown("""
    **Objectif :**  
    Ce projet vise à construire un modèle d'apprentissage automatique pour prédire l'espèce d'une fleur d'iris en fonction de plusieurs caractéristiques physiques telles que la longueur et la largeur du sépale, ainsi que la longueur et la largeur du pétale. Le projet couvre les différentes étapes du processus d'apprentissage automatique :
    """)
    col1, col2 = st.columns([1, 2])
    
    with col1:
    # Liste des étapes du projet
        st.subheader("🔍 Étapes du projet :")
        st.write("""
        1. **Exploration du Dataset**  
        Nous commençons par charger et explorer le jeu de données Iris pour en comprendre la structure, le contenu et les caractéristiques clés.

        2. **Nettoyage des données et Prétraitement**  
        Cette étape consiste à traiter les valeurs manquantes, les valeurs aberrantes et à normaliser les données pour les rendre prêtes à être utilisées pour l'entraînement du modèle.

        3. **Analyse Exploratoire des Données (EDA)**  
        Nous visualisons les données et effectuons une analyse statistique pour identifier les motifs, les tendances et les relations dans les données.

        4. **Entraînement et Évaluation du Modèle**  
        Nous entraînons différents modèles d'apprentissage automatique, évaluons leur performance et sélectionnons le meilleur modèle en fonction des métriques comme la précision et la performance.

        5. **Prédiction**  
        Une fois le meilleur modèle sélectionné, nous l'utilisons pour effectuer des prédictions sur de nouvelles données.

        6. **Conclusion**  
        Nous récapitulons nos résultats, discutons des performances du modèle et proposons des pistes pour les futures améliorations.
        """)
        # Aspect visuel avec image ou illustration (facultatif)
        st.subheader("🌱 Le pipeline de Data Science")
        st.image("userProfile.jpg", caption="Le pipeline de Data Science")

    with col2:
    # Technologies et outils utilisés
        st.subheader("🛠️ Technologies et outils utilisés")
        st.write("""
    - **Python** : Langage principal utilisé pour la manipulation des données et le développement des modèles d'apprentissage automatique.
    - **Streamlit** : Framework puissant pour créer des applications web interactives.
    - **Pandas** : Utilisé pour la manipulation et l'analyse des données.
    - **Scikit-learn** : Bibliothèque d'apprentissage automatique utilisée pour l'entraînement des modèles, l'évaluation et la prédiction.
    - **Matplotlib & Seaborn** : Outils utilisés pour la visualisation des données et l'analyse exploratoire des données.
    - **Joblib** : Utilisé pour sauvegarder et charger les modèles d'apprentissage automatique.
    """)

        # Remerciements
        st.subheader("🤝 Remerciements")
        st.write("""
        - Le jeu de données Iris utilisé dans ce projet est disponible publiquement et est un jeu de données standard en apprentissage automatique.
        - Merci à la communauté open-source pour les bibliothèques et outils qui ont rendu ce projet possible.
        """)

        # Footer et appel à l'action
        st.markdown("---")
        st.markdown("""
        **Explorez le reste de l'application** pour plonger plus profondément dans le flux de travail du projet.  
        Utilisez la barre latérale pour naviguer à travers différentes sections comme Dataset, EDA, et Machine Learning.
        """)
