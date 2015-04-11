from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def home(request):
	return render(request,'services/home.html')


from .models import Enseignant
def liste_enseignants(request):

	liste = Enseignant.objects.all()
	return render(request, 'services/enseignants.html',{'date': timezone.now(), 'Enseignants' : liste})


from .models import Ue
def liste_ue(request):
	liste = Ue.objects.all()
	return render(request, 'services/ue.html',{'date': timezone.now(), 'Ue' : liste})


from .models import Tache
def liste_taches(request):
	liste = Tache.objects.all()
	return render(request, 'services/taches.html',{'date': timezone.now(), 'Taches' : liste})

from .forms import EnseignantForm
def nouvelens(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = EnseignantForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = EnseignantForm()  # Nous créons un formulaire vide

    return render(request, "services/ens_form.html", locals())

from .forms import UeForm
def nouvelleue(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = UeForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = UeForm()  # Nous créons un formulaire vide

    return render(request, "services/ue_form.html", locals())

