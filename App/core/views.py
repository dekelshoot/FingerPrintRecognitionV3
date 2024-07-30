from tkinter import E
from django.shortcuts import render
from django.views import View

from .forms import MonImageForm
from .image import MonImage
import pickle
import numpy as np

from .models import Image

from keras.models import load_model


# Create your views here.

class PrintView(View):

    template_name = "core/save.html"

    def get(self, request, *args, **kwargs):

        form = MonImageForm()
        context = {"form": form}
        return render(request, self.template_name, context)
    

    def get_name_from_classe(self, classe):
            
        dictionnaire_correspondance_label = {"Belviane":0, "Dekel":1, "Manuella":2, "Nelson":3, "Voltaire":4}
        
        for key, val in dictionnaire_correspondance_label.items():
            if val == classe:
                return key
        return None


    def post(self, request, *args, **kwargs):

        form = MonImageForm(request.POST, request.FILES)
        x_test_data = []
        
        if form.is_valid():
            image = form.cleaned_data['image'] # image entreee
            id_image = form.save() # je sauvegarde l'image entree
            image = Image.objects.get(id = id_image) # je recupere l'image entree
            path = image.path.path # je recupere le chemin d'acces a cette image entree la
            image = MonImage(path) # je transfome en  mon objet image facilement manipulable pour extraction de caracteristiques
            car_image = image.extraire_caracteristique() #j'extrais donc les caracteristiques
            x_test_data.append(car_image) # je suaveegarde ces caracteristiques 
            x_test_data = np.array(x_test_data) # je mets les caracteristiques sous la bonne forme pour passer au modele
            
            model = load_model('model.h5') # j'importe le modele entrainé

            predictions = model.predict(x_test_data) # je fais les predictions

            classe_predite = np.argmax(predictions, axis=1)[0] # je recupere la prediction (le numero de la classe)
            print(predictions,  " classe predite")

            classe = self.get_name_from_classe(classe_predite) #je recupere le nom de la personne correspondante

            return render(request, self.template_name, {"classe":classe, "form":"form"})

        else:
            print(form.errors)
            context = {"form" : form}
            return render(request, self.template_name, context)