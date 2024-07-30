import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import backend as K

NUM_CLASSES = 5


from google.colab import drive
drive.mount('/content/drive')


# Charger le vecteur de car de test
with open('/content/drive/MyDrive/x_test_data.pkl', 'rb') as fichier:
    x_test_data = fichier.read()


# Charger le vecteur de car d'entrainement
with open('/content/drive/MyDrive/x_train_data.pkl', 'rb') as fichier:
    x_train_data = fichier.read()


# Charger le vecteur de label de test
with open('/content/drive/MyDrive/y_test_data.pkl', 'rb') as fichier:
    y_test_data = fichier.read()


# Charger le vecteur de label d'entrainement
with open('/content/drive/MyDrive/y_train_data.pkl', 'rb') as fichier:
    y_train_data = fichier.read()


# Désérialiser les vecteurs
x_train_data = np.array(pickle.loads(x_train_data))
y_train_data = np.array(pickle.loads(y_train_data))
x_test_data = np.array(pickle.loads(x_test_data))
y_test_data = np.array(pickle.loads(y_test_data))


# Conversion des classes en représentation catégorique (one-hot encoding)
y_train_cat = keras.utils.to_categorical(y_train_data, num_classes=NUM_CLASSES)
print(type(y_train_cat))

# Création du modèle
model = keras.models.Sequential([
    keras.layers.Dense(300, activation='relu', input_shape=(None, 1,len(x_train_data[0]))),
    keras.layers.Dense(130, activation='relu'),
    keras.layers.Dense(140, activation='relu'),
    keras.layers.Dense(150, activation='relu'),
    keras.layers.Dense(150, activation='relu'),
    keras.layers.Dense(160, activation='relu'),
    keras.layers.Dense(160, activation='relu'),
    keras.layers.Dense(180, activation='relu'),
    keras.layers.Dense(180, activation='relu'),
    keras.layers.Dense(180, activation='relu'),
    keras.layers.Dense(200, activation='relu'),
    keras.layers.Dense(200, activation='relu'),
    keras.layers.Dense(200, activation='relu'),
    keras.layers.Dense(NUM_CLASSES, activation='softmax', input_shape=(1,len(x_train_data[0])))  # Couche de sortie avec activation softmax pour la classification multiclasse
])


# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(x_train_data, y_train_cat, epochs=100, batch_size=1)

# Prédictions sur les données de test
predictions = model.predict(x_test_data)

# Conversion des prédictions en classes prédites
classes_predites = np.argmax(predictions, axis=1)

# Affichage des classes prédites
print("Classes prédites :", classes_predites)

model.save('/content/drive/MyDrive/model.h5')


