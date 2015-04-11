from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request,'services/home.html')

def enseignants(request):
	return render(request, 'services/enseignants.html')