from Image import MonImage
import os
import csv
import pickle
import time
import numpy as np
from numpy.random import shuffle


# Début du chronomètre
start_time = time.time()


path_images = ["../labelises/B/", "../labelises/D/", "../labelises/M/", "../labelises/N/", "../labelises/V/"]
x_train = []
y_train = []
dictionnaire_correspondance_label = {"B":0, "D":1, "M":2, "N":3, "V":4}

# Chemin du fichier de sortie
output_file = "caracteristiques.csv"

 # Ouvrir le fichier en mode écriture
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Écrire l'en-tête du fichier CSV (facultatif)
    writer.writerow(["classe", "Nom de l'image", "Vecteur de caractéristiques"])

    for path in path_images:

        # Trier les fichiers par ordre alphabétique
        print(path)
        sorted_files = sorted(os.listdir(path), key=lambda x: int(x.split('.')[0]))
        
        for img in sorted_files:
            
            if img.split(".")[1] == "pgm":
                continue
            path_image = os.path.join(path, img)
            image = MonImage(path_image=path_image)
            
            caracteristique = image.extraire_caracteristique()

            # Écrire les données de l'image et du vecteur de caractéristiques dans le fichier CSV
            writer.writerow([path[-2], img, caracteristique])

            x_train.append(caracteristique)
            y_train.append(dictionnaire_correspondance_label[path[-2]])
            
            print("deja a l'image : ", img, " du repertoire ", path[-2] )


# Calcul de l'index de séparation (pour segmenter les donnees)
split_index = int(len(x_train) * 0.9)

# transformons les donnees en array numpy
x_train = np.array(x_train)
y_train = np.array(y_train)

# Concaténer X_train et y_train en une seule matrice
data = np.column_stack((x_train, y_train))

# Mélanger les données
shuffle(data)

# Séparer les caractéristiques (X) et les étiquettes (y) après le mélange
x = data[:, :-1]
y = data[:, -1]

# Diviser le vecteur en vecteur d'entrainement et de test 
x_train_data = x[:split_index]
x_train_data_serialise = pickle.dumps(x_train_data)

y_train_data = y[:split_index]
y_train_data_serialise = pickle.dumps(y_train_data)

x_test_data = x[split_index:]
x_test_data_serialise = pickle.dumps(x_test_data)

y_test_data = y[split_index:]
y_test_data_serialise = pickle.dumps(y_test_data)


# Enregistrer les données sérialisées d'entrainement dans un fichier pkl
with open('x_train_data.pkl', 'wb') as fichier:
    fichier.write(x_train_data_serialise)

# Enregistrer les labels sérialisées d'entrainement dans un fichier pkl
with open('y_train_data.pkl', 'wb') as fichier:
    fichier.write(y_train_data_serialise)


# Enregistrer les données sérialisées de test dans un fichier pkl
with open('x_test_data.pkl', 'wb') as fichier:
    fichier.write(x_test_data_serialise)

# Enregistrer les labels sérialisées de test dans un fichier pkl
with open('y_test_data.pkl', 'wb') as fichier:
    fichier.write(y_test_data_serialise)

# Fin du chronomètre
end_time = time.time()


# Calcul de la durée d'exécution en secondes
execution_time = end_time - start_time
print(f"Temps d'exécution : {execution_time} secondes")