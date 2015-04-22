from django import forms
from .models import Enseignant, Ue, Tache

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        exclude = ()

class UeForm(forms.ModelForm):
    class Meta:
        model = Ue
        exclude = ()

class TacheForm(forms.ModelForm):

    class Meta:
        model = Tache
        exclude = ()



	
    