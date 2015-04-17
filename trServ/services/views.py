from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from django.views import generic
from .models import Enseignant, Tache, Ue
from .forms import EnseignantForm, UeForm
#-----------------------------------------------
# acceuil

def home(request):
	return render(request,'services/home.html',{'datetime': timezone.now()})

#-----------------------------------------------
# Affichage par liste

class EnseignantListView(generic.ListView):
    model = Enseignant

    def get_context_data(self, **kwargs):
        context = super(EnseignantListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def liste_enseignants(request):
	order_by = request.GET.get('order_by', 'grade')
	liste_ens = Enseignant.objects.order_by(order_by)
	return render(request, 'services/enseignants.html',{'datetime': timezone.now(), 'Enseignants' : liste_ens})


def liste_ue(request):
	liste_ue = Ue.objects.order_by('année','semestre')
	return render(request, 'services/ue.html',{'datetime': timezone.now(), 'Ue' : liste_ue})


def liste_taches(request):
	order_by = request.GET.get('order_by', 'ue')
	liste = Tache.objects.all().order_by(order_by)
	return render(request, 'services/taches.html',{'datetime': timezone.now(), 'Taches' : liste})



#-----------------------------------------------
# Affichage un(e) seul(e)


class tache_detail(generic.DetailView):
    model = Tache
    template_name = 'services/tache_detail.html'


def une_ue(request,pk):
	return render(request, "services/une_ue.html", {'ue': Ue.objects.get(id=pk),'datetime': timezone.now()})

def un_enseignant(request,pk):
	return render(request, "services/un_ens.html", {'ens': Enseignant.objects.filter(id=pk)[0], 'datetime': timezone.now()})



#-----------------------------------------------
# Formulaires

def ens_form(request,pk):
	return render(request, "services/ens_form.html", {'ens': Enseignant.objects.get(id=pk) , 'datetime': timezone.now()})


def ue_form(request,pk):
	return render(request, "services/ue_form.html", {'ue': Ue.objects.get(id=pk) , 'datetime': timezone.now()})




def nouvelens(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = EnseignantForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = EnseignantForm()  # Nous créons un formulaire vide

	return render(request, "services/ens_form.html",{'datetime': timezone.now()})


def nouvelleue(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = UeForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = UeForm()  # Nous créons un formulaire vide

	return render(request, "services/ue_form.html", locals(), {'datetime': timezone.now()})




