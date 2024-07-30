from django import forms

from .models import Image


class MonImageForm(forms.Form):

    image = forms.ImageField(required=True)

    def save(self):

        image = Image.objects.create(path = self.cleaned_data['image'])
        return image.id
        
    