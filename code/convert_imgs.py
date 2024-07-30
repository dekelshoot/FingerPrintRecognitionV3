from PIL import Image
import os

def convert_png_to_pgm(png_path, pgm_path):
    # Ouvrir l'image PNG
    image = Image.open(png_path)
    
    # Convertir en niveaux de gris
    image_grayscale = image.convert('L')
    
    # Obtenir les dimensions de l'image
    width, height = image_grayscale.size
    
    # Ouvrir le fichier PGM en mode écriture
    with open(pgm_path, 'w') as pgm_file:
        # Écrire l'en-tête PGM
        pgm_file.write("P2\n")
        pgm_file.write(f"# Created by MsrVolt\n")
        pgm_file.write(f"{width} {height}\n")
        pgm_file.write("255\n")
        
        # Écrire les valeurs de luminosité des pixels
        for y in range(height):
            for x in range(width):
                pixel_value = image_grayscale.getpixel((x, y))
                pgm_file.write(f"{pixel_value} ")
                pgm_file.write("\n")


# conversion de toutes les images png en images pgm
PATH_PNG = "../images_png/"
PATH_PGM = "../images_pgm/"
indice_nommage_pgm = 0

for img in os.listdir(PATH_PNG):
    indice_nommage_pgm = indice_nommage_pgm + 1

    png_path = PATH_PNG+img
    pgm_path = PATH_PGM+str(indice_nommage_pgm)+".pgm"

    print(png_path, pgm_path)

    convert_png_to_pgm(png_path, pgm_path)
