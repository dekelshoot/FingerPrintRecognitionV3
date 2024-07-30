from __future__ import division
import numpy as np
import PIL
from PIL import Image
import math

class MonImage():

    # constructeur
    def __init__(self, path_image = "", pgm_path = ""):

        self.path_image = path_image
        self.pgm_path = pgm_path
        self.matrice_image = []
        self.matrice_lbp = []
        self.nb_colonnes = 0
        self.nb_lignes = 0


    # fonction pour obtenir l'image pgm(a partir de ce qui a ete obtenu, pgm ou png)
    def obtenir_image_pgm(self,):

        self.pgm_path = self.path_image.rsplit('.', 1)[0] + ".pgm" # je cree le fichier pgm avec le meme nom que le png en changeant juste l'extension

        # Ouvrir l'image PNG
        try:
            image = Image.open(self.path_image)
        except PIL.UnidentifiedImageError:
            self.pgm_path = self.path_image
            return
        
        # Convertir en niveaux de gris
        image_grayscale = image.convert('L')
        
        # Obtenir les dimensions de l'image
        width, height = image_grayscale.size

        self.nb_lignes = height
        self.nb_colonnes = width
        
        # Ouvrir le fichier PGM en mode écriture
        with open(self.pgm_path, 'w') as pgm_file:
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

    
    # obtenir a matrice de l'image a partir du fichier image
    def obtenir_matrice(self):

        if self.pgm_path == "":
            print("Vous devez fournir une image pgm, ou alors convertir cette image au prealable en utilisant la fonction obtenir_image_pgm() ")
            return

        with open(self.pgm_path, "r") as file:
            lines = file.readlines()
            lines = lines[2:]
            nb_col, nb_lig = map(int, lines[0].split())
            resolution = lines[1]
            lines = lines[2:]
            
            self.matrice_image = np.zeros((nb_lig, nb_col))
            
            k = 0
            for i in range(nb_lig):
                for j in range(nb_col):
                    self.matrice_image[i,j] = lines[k]
                    k = k+1


    # Fonction de seuillage: si la difference est inferieure ou egale a 0, on met 0 sinon on met 1
    def functionS(self, val):

        if val <= 0:
            return 0
        else:
            return 1


    # calcule la matrice lbp associee a l'image, en tenant cmpte d'un voisinage de distance 1, tenant cmpte des pixels voisins de la gauche vers la droite et du haut vers le bas
    def calcul_matrice_lbp(self):

        nb_lig = len(self.matrice_image)
        nb_col = len(self.matrice_image[0])

        for _ in range(nb_lig):
            ligne = [0] * nb_col
            self.matrice_lbp.append(ligne)
        
        for i in range(nb_lig):
            for j in range(nb_col):
                # pour esquiver le pixels de bordures
                if i == 0:
                    self.matrice_lbp[i][j] = 0
                    continue
                elif j == 0:
                    self.matrice_lbp[i][j] = 0
                    continue
                elif i == nb_lig-1:
                    self.matrice_lbp[i][j] = 0
                    continue
                elif j == nb_col-1:
                    self.matrice_lbp[i][j] = 0
                    continue
                else:
                    dif1 = self.matrice_image[i-1][j] - self.matrice_image[i+1][j]
                    seuillage1 = self.functionS(dif1)
                    poids_lbp_voisin_1 = 2**0
                    dif2 = self.matrice_image[i-1][j+1] - self.matrice_image[i+1][j-1]
                    seuillage2 = self.functionS(dif2)
                    poids_lbp_voisin_2 = 2**1
                    dif3 = self.matrice_image[i][j+1] - self.matrice_image[i][j-1]
                    seuillage3 = self.functionS(dif3)
                    poids_lbp_voisin_3 = 2**2
                    dif4 = self.matrice_image[i+1][j+1] - self.matrice_image[i-1][j-1]
                    seuillage4 = self.functionS(dif4)
                    poids_lbp_voisin_4 = 2**3

                    poids_lbp_pixel_central = seuillage1*poids_lbp_voisin_1 + seuillage2*poids_lbp_voisin_2 + seuillage3*poids_lbp_voisin_3 + seuillage4*poids_lbp_voisin_4
                    self.matrice_lbp[i][j] = poids_lbp_pixel_central

        self.matrice_lbp = np.array(self.matrice_lbp)
        

    # fonction qui prends en paramentre la matrice de l'image, les dimmensions des blocs en lesquels on veut segmenter (nombre de lignes et nombre de colonnes),
    # Elle prends aussi le nombre de carreaux de chevauchement(en ligne et en colonne) puis elle retourne la liste des differents blocs (liste de matrices).
    # par defaut, on segmente en blocs de 10(en ligne et en colonne) sans chevauchement entre les blocs
    def segmenter_en_blocs(self, nb_ligne_bloc = 10, nb_colonne_bloc = 10, nb_carreaux_chev_lignes = 0, nb_carreaux_chev_colonnes = 0) -> list: 

        nb_lig = len(self.matrice_lbp)
        nb_col = len(self.matrice_lbp[0])
        
        ligne_debut_bloc = 0
        tous_les_blocs = []

        pas_en_colonne = nb_colonne_bloc - nb_carreaux_chev_colonnes # nombre de carreaux varie en fonction du nombre de carreaux qui doivent se chevaucher
        pas_en_ligne = nb_ligne_bloc - nb_carreaux_chev_lignes # nombre de carreaux varie en fonction du nombre de carreaux qui doivent se chevaucher

        for ligne in range(nb_ligne_bloc, nb_lig, pas_en_ligne):
            # print("voici i ", ligne, "\n")
            colonne_debut_bloc = 0
            ligne_fin_bloc = ligne
            for colonne in range(nb_colonne_bloc, nb_col, pas_en_colonne):
                # print("voici j ", colonne)
                colonne_fin_bloc = colonne 
                
                # print("ligne debut", ligne_debut_bloc, "ligne_fin_bloc", ligne_fin_bloc)
                # print("colonne debut", colonne_debut_bloc, "colonne_fin_bloc", colonne_fin_bloc, "\n")
                new_bloc = self.matrice_lbp[ligne_debut_bloc:ligne_fin_bloc,colonne_debut_bloc:colonne_fin_bloc]
                tous_les_blocs.append(new_bloc)

                colonne_debut_bloc = colonne_fin_bloc - nb_carreaux_chev_colonnes
                # print("j'ai change colonne debut en ", colonne_debut_bloc)

                # je verifie si le prochain bloc peut se former, sinon je forme le dernier loc avec les "nb_colonne_bloc" dernieres colonnes possibles
                if colonne_fin_bloc + pas_en_colonne >= nb_col:
                    colonne_debut_bloc = nb_col - nb_colonne_bloc
                    colonne_fin_bloc = nb_col
                    # print("ligne debut", ligne_debut_bloc, "ligne_fin_bloc", ligne_fin_bloc)
                    # print("colonne debut", colonne_debut_bloc, "colonne_fin_bloc", colonne_fin_bloc, "\n")
                    new_bloc = self.matrice_lbp[ligne_debut_bloc:ligne_fin_bloc,colonne_debut_bloc:colonne_fin_bloc]
                    tous_les_blocs.append(new_bloc)

            ligne_debut_bloc = ligne_fin_bloc - nb_carreaux_chev_lignes

            # je verifie si le prochain bloc peut se former, sinon je forme le dernier bloc avec les "nb_ligne_bloc" dernieres lignes possibles, en tenant compte de toutes les colonnes
            if ligne_fin_bloc + pas_en_ligne >= nb_lig :
                # print("voici i ", ligne_debut_bloc)
                ligne_debut_bloc = nb_lig - nb_ligne_bloc
                ligne_fin_bloc = nb_lig

                colonne_debut_bloc = 0
                for colonne in range(nb_colonne_bloc, nb_col, pas_en_colonne):
                    # print("voici j ", colonne)

                    colonne_fin_bloc = colonne
                    
                    # print("ligne debut", ligne_debut_bloc, "ligne_fin_bloc", ligne_fin_bloc)
                    # print("colonne debut", colonne_debut_bloc, "colonne_fin_bloc", colonne_fin_bloc, "\n")
                    new_bloc = self.matrice_lbp[ligne_debut_bloc:ligne_fin_bloc,colonne_debut_bloc:colonne_fin_bloc]
                    tous_les_blocs.append(new_bloc)

                    colonne_debut_bloc = colonne_fin_bloc - nb_carreaux_chev_colonnes

                    if colonne_fin_bloc + pas_en_colonne >= nb_col:
                        colonne_debut_bloc = nb_col - nb_colonne_bloc
                        colonne_fin_bloc = nb_col
                        # print("ligne debut", ligne_debut_bloc, "ligne_fin_bloc", ligne_fin_bloc)
                        # print("colonne debut", colonne_debut_bloc, "colonne_fin_bloc", colonne_fin_bloc, "\n")
                        new_bloc = self.matrice_lbp[ligne_debut_bloc:ligne_fin_bloc,colonne_debut_bloc:colonne_fin_bloc]
                        tous_les_blocs.append(new_bloc)
        
        return tous_les_blocs


    def histogramme(self, img_bloc, resolution_bloc = 15) -> list:

        resolution_bloc = resolution_bloc + 1
        histo = [0] * resolution_bloc

        nb_lig = len(img_bloc)
        nb_col = len(img_bloc[0])

        for ligne in range(nb_lig):
            for colonne in range(nb_col):
                histo[img_bloc[ligne][colonne]] += 1
        
        return  histo

    # fonction qui a partir de l'image pgm, extrai
    def extraire_caracteristique(self, nb_blocs = 16, nb_carreaux_chev_lignes = 0, nb_carreaux_chev_colonnes = 0):

        diviseur = math.isqrt(nb_blocs) # pour avoir le resultat en int genre 5 au lieu de 5.0 pour ne pas baffouer ma condition du bas
        if type(diviseur) != int:
            print("le nombre de blocs doit etre un carre parfait")
            return
        self.obtenir_image_pgm() # pour m'assure que j'ai bien l'image pgm
        self.obtenir_matrice() # j'obtiens l'image en matrice
        self.calcul_matrice_lbp() # je calcule la matrice lbp, que je vais segmenter et calculer l'histogramme de chacun de ces blocs, pour extraire en fin les caracteristiques de l'image
        blocs = self.segmenter_en_blocs(nb_ligne_bloc = math.ceil(self.nb_lignes/diviseur), nb_colonne_bloc = math.ceil(self.nb_colonnes/diviseur), nb_carreaux_chev_lignes = nb_carreaux_chev_lignes, nb_carreaux_chev_colonnes = nb_carreaux_chev_colonnes)
        
        # je parcours les blocs de l'image, pour extraire les histogrammes, je les concatene pour avoir le vecteur de caracteristique, et je stocke ca
        vecteur_caracteristiques = []
        for bloc in blocs:

            histo_i = self.histogramme(bloc)
            vecteur_caracteristiques.extend(histo_i)
        
        print(len(blocs))
        return vecteur_caracteristiques


