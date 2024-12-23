import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

# Créer un graphique avec NetworkX
G = nx.DiGraph()

# Ajouter des nœuds
G.add_node("Acquisition des Données")
G.add_node("Nettoyage des Données")
G.add_node("Exploration des Données (EDA)")
G.add_node("Modélisation (Machine Learning)")
G.add_node("Évaluation du modèle")
G.add_node("Optimisation du modèle")
G.add_node("Déploiement du modèle")
G.add_node("Suivi et maintenance du modèle")

# Ajouter des arêtes (les liens entre les nœuds)
G.add_edges_from([("Acquisition des Données", "Nettoyage des Données"),
                 ("Nettoyage des Données", "Exploration des Données (EDA)"),
                 ("Exploration des Données (EDA)", "Modélisation (Machine Learning)"),
                 ("Modélisation (Machine Learning)", "Évaluation du modèle"),
                 ("Évaluation du modèle", "Optimisation du modèle"),
                 ("Optimisation du modèle", "Déploiement du modèle"),
                 ("Déploiement du modèle", "Suivi et maintenance du modèle")])

# Définir le layout du graphique
pos = nx.spring_layout(G)

# Dessiner le graphique
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)

# Sauvegarder l'image dans un fichier
image_path = "pipeline_data_science.png"
plt.savefig(image_path)

# Afficher l'image dans Streamlit
st.title("Pipeline de Data Science")
st.image(image_path, caption="Le Pipeline de Data Science")

# Optionnel : Afficher l'image aussi avec Streamlit
st.pyplot(plt)
