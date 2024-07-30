import pickle
import numpy as np

NUM_CLASSES = 5


# Charger le vecteur de car de test
with open('x_test_data.pkl', 'rb') as fichier:
    x_test_data = fichier.read()


# Charger le vecteur de car d'entrainement
with open('x_train_data.pkl', 'rb') as fichier:
    x_train_data = fichier.read()


# Charger le vecteur de label de test
with open('y_test_data.pkl', 'rb') as fichier:
    y_test_data = fichier.read()


# Charger le vecteur de label d'entrainement
with open('y_train_data.pkl', 'rb') as fichier:
    y_train_data = fichier.read()


# Désérialiser les vecteurs
x_train_data = pickle.loads(x_train_data)
y_train_data = pickle.loads(y_train_data)
x_test_data = pickle.loads(x_test_data)
y_test_data = pickle.loads(y_test_data)


print("le train\n")
print("X")
print(len(x_train_data))
#print(x_train_data)
print("Y")
print(len(y_train_data))
print(y_train_data)


print("le test\n")
print("X")
print(len(x_test_data))
#print(x_test_data)
print("Y")
print(len(y_test_data))
print(y_test_data)


