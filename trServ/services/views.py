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