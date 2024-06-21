# Projet de Sauvegarde Automatisée et Application Web de Saisie de Données

## Présentation

Ce projet a pour but de mettre en place une solution de sauvegarde automatisée pour assurer la sécurité et la pérennité des données, ainsi qu'une application web permettant de saisir, sauvegarder et restaurer des données textuelles. 

## Fonctionnalités

- **Application Web** :
  - Interface simple pour saisir et afficher des données textuelles.
  - Sauvegarde automatique des données toutes les 10 secondes.
  - Affichage de l'heure de la dernière sauvegarde.

- **Sauvegarde et Restauration** :
  - Sauvegarde automatisée des données sur le disque local.
  - Restauration des données depuis la dernière sauvegarde.

## Prérequis

- **Windows** :
  - Powershell
  - Python 3
  - Flask (installable via pip)
  - Serveur web accessible sur le réseau (port 80)
  
## Structure des Fichiers

C:\MyWebApp/
│
├── backup.ps1
├── restore.ps1
├── main.py
├── data.txt (créé automatiquement lors de la première sauvegarde)
├── timestamp.txt (créé automatiquement lors de la première sauvegarde)
│
└── templates/
└── index.html


## Installation

1. **Cloner le projet & installer la librairie flask** :

```bash
   git clone https://github.com/votre-repo/MyWebApp.git
   cd MyWebApp
   pip install flask
```

2. **Configuration du Réseau** :

Pour accéder à l'application web depuis d'autres machines sur le même réseau :

Configurer la machine virtuelle :

- Accédez aux paramètres de votre machine virtuelle.
- Allez dans la section Réseau.
- Sélectionnez "Accès par pont".
- Choisissez l'adaptateur réseau correct (celui connecté à Internet).

Vérifier l'adresse IP :

- Exécutez ipconfig sur votre machine hôte et sur la machine virtuelle.
- Notez les adresses IPv4 respectives pour vérifier qu'elles sont sur le même sous-réseau.


## Exécution

1. **Lancer l'application Flask** :

```bash
python main.py
```
L'application sera accessible à l'adresse http://[Adresse-IP-de-votre-machine-virtuelle].

2. **Accéder à l'application web** :

Ouvrez un navigateur web et accédez à l'adresse http://[Adresse-IP-de-votre-machine-virtuelle].


## Sauvegarde Automatisée

- Le script `backup.ps1` permet de sauvegarder automatiquement les données.
- Le script `restore.ps1` permet de restaurer les données depuis la dernière sauvegarde.


## Utilisation

1. **Saisie de données** :

- Accédez à l'application web via votre navigateur.
- Entrez le texte souhaité dans la zone de texte.

2. **Sauvegarde automatique** :

- Les données sont sauvegardées automatiquement toutes les 10 secondes.

3. **Restaurer les données** :

- Exécutez le script `restore.ps1` pour restaurer les données depuis la dernière sauvegarde (exécution automatique lors du lancement du fichier `app.py`).


## Documentation

Pour la restauration :

- Assurez-vous que le script `restore.ps1` est correctement configuré avec les chemins de source et de destination.
- Exécutez le script `restore.ps1` via Powershell pour restaurer les données.


## Conclusion

Ce projet permet de sécuriser et pérenniser les données saisies via une interface web simple. Grâce à la sauvegarde automatisée, les données sont protégées et peuvent être restaurées en cas de besoin.
