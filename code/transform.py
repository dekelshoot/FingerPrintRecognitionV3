"""
from PIL import Image

# Charger l'image
image = Image.open('../1.jpg')

# Convertir l'image en niveaux de gris
image_gris = image.convert('L')

# Enregistrer l'image convertie en niveaux de gris
image_gris.save('../1_2.jpg')

"""

from Image import MonImage

i = MonImage("../1.jpg")
print(len(i.extraire_caracteristique()))
