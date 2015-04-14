from django.shortcuts import render
from django.utils import timezone


# Create your views here.


def home(request):
	return render(request,'services/home.html',{'datetime': timezone.now()})


from .models import Enseignant
def liste_enseignants(request):
	liste_ens = Enseignant.objects.order_by('nom')
	return render(request, 'services/enseignants.html',{'datetime': timezone.now(), 'Enseignants' : liste_ens})


from .models import Ue
def liste_ue(request):
	liste_ue = Ue.objects.order_by('année','semestre')
	return render(request, 'services/ue.html',{'datetime': timezone.now(), 'Ue' : liste_ue})


from .models import Tache
def liste_taches(request):
	liste = Tache.objects.all()
	return render(request, 'services/taches.html',{'datetime': timezone.now(), 'Taches' : liste})

from .forms import EnseignantForm
def nouvelens(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = EnseignantForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = EnseignantForm()  # Nous créons un formulaire vide

	return render(request, "services/ens_form.html", locals(),{'datetime': timezone.now()})

from .forms import UeForm
def nouvelleue(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = UeForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = UeForm()  # Nous créons un formulaire vide

	return render(request, "services/ue_form.html", locals(), {'datetime': timezone.now()})


def une_ue(request,code):
	return render(request, "services/une_ue.html", {'code': code},{'datetime': timezone.now()})


