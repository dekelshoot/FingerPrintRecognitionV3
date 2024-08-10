# FingerPrintRecognitionV3

Bienvenue dans le projet **FingerPrintRecognitionV3** ! Dans ce dépôt, vous trouverez tout le code nécessaire pour créer un système de reconnaissance d'empreintes digitales utilisant l'intelligence artificielle. Ce projet a été développé pour capturer des empreintes digitales, extraire leurs caractéristiques, et les utiliser pour entraîner un modèle de machine learning capable de les reconnaître avec une grande précision.

## Table des Matières

- [Aperçu du Projet](#aperçu-du-projet)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

## Aperçu du Projet

Ce projet a pour objectif de démontrer comment les empreintes digitales peuvent être capturées, traitées, et utilisées pour entraîner un modèle de reconnaissance. Voici les principales étapes couvertes par ce dépôt :

1. **Collecte des Empreintes Digitales** : Utilisation d'encre, de papier, et d'une caméra de smartphone pour capturer les empreintes.
2. **Prétraitement des Images** : Conversion des images en niveaux de gris et extraction des caractéristiques avec l'algorithme LBP (Local Binary Patterns).
3. **Construction du Modèle** : Création et entraînement d'un réseau de neurones pour la reconnaissance des empreintes.
4. **Création d'une Application Web** : Développement d'une application web avec Django pour tester le modèle.

## Technologies Utilisées

- **Python** : Langage principal utilisé pour le traitement des images et l'implémentation du modèle de machine learning.
- **OpenCV** : Bibliothèque utilisée pour le traitement des images.
- **Django** : Framework web utilisé pour créer l'application web permettant de tester le modèle.
- **pickle** : Pour la sérialisation et la désérialisation des objets Python.
- **numpy** : Pour les opérations numériques et le traitement des matrices.
- **tensorflow** et **keras** : Pour la création et l'entraînement du réseau de neurones.


## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/dekelshoot/FingerPrintRecognitionV3.git
   cd FingerPrintRecognitionV3 

2. Accédez au répertoire du projet :

```bash
cd FingerPrintRecognitionV3
```

3. Installez les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

4. Lancez l'application Django :
```bash
cd App
python manage.py runserver
```

## Utilisation
Collecte des empreintes digitales : Suivez les instructions dans la vidéo pour capturer les empreintes digitales avec de l'encre et du papier.
Soumission de l'image : Utilisez l'application web pour soumettre une image d'empreinte digitale.
Prédiction : Le modèle prédit à qui appartient l'empreinte digitale en se basant sur les caractéristiques extraites.
Contribution
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des modifications que vous souhaitez apporter.

# License
Ce projet est sous licence MIT. 

## Liens
- [Vidéo YouTube ](https://youtu.be/yh2qBzH6K1o?si=09ZsR93DQgtjPtgU)
- [Script](https://docs.google.com/document/d/10Zzer97zm06T_scWQ0ZhP3zzZBzthV_Obgqc4yXCuRU/edit?usp=sharing)
