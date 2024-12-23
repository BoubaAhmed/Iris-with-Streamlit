from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def make_predictions(model, X):
    return model.predict(X)
