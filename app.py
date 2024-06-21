from flask import Flask, request, render_template, redirect, url_for  # Importation des modules nécessaires de Flask
import os  # Module pour les opérations sur le système de fichiers
from datetime import datetime  # Module pour gérer les dates et heures

app = Flask(__name__)  # Création d'une instance de l'application Flask

# Chemin des fichiers de données et de timestamp
DATA_FILE = "data.txt"
TIMESTAMP_FILE = "timestamp.txt"

# Fonction pour sauvegarder les données et l'heure actuelle
def save_data(data):
    # Sauvegarde des données dans le fichier DATA_FILE
    with open(DATA_FILE, "w") as file:
        file.write(data)
    # Sauvegarde de l'heure dans le fichier TIMESTAMP_FILE
    with open(TIMESTAMP_FILE, "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Fonction pour charger les données et l'heure de la dernière sauvegarde
def load_data():
    # Lecture des données depuis le fichier DATA_FILE
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            data = file.read()
    else:
        data = ""
    # Lecture de l'heure de la dernière sauvegarde depuis le fichier TIMESTAMP_FILE
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, "r") as file:
            timestamp = file.read()
    else:
        timestamp = "N/A"
    return data, timestamp

# Définition de la route principale
@app.route('/', methods=['GET', 'POST'])
def index():
    # Si la méthode de la requête est POST, l'utilisateur a soumis des données
    if request.method == 'POST':
        data = request.form['content']  # Récupération des données soumises
        save_data(data)  # Sauvegarde des données
        return redirect(url_for('index'))  # Redirection vers la route principale pour éviter les resoumissions de formulaire
    # Si la méthode de la requête est GET, chargement des données et de l'heure de la dernière sauvegarde
    data, timestamp = load_data()
    return render_template('index.html', data=data, timestamp=timestamp)  # Rendu de la template avec les données et l'heure de sauvegarde

# Lancement
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)