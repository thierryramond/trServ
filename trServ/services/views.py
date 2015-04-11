from django.shortcuts import render
from django.utils import timezone

# Create your views here.


def home(request):
	return render(request,'services/home.html')


from .models import Enseignant
def liste_enseignants(request):

	liste = Enseignant.objects.all()
	return render(request, 'services/enseignants.html',{'date': timezone.now(), 'Enseignants' : liste})