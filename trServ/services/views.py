from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
from django.views import generic
from .models import Enseignant, Tache, Ue
from .forms import EnseignantForm, UeForm, TacheForm
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
	order_by = request.GET.get('order_by', 'bilan')
	liste_ens = Enseignant.objects.order_by(order_by)
	return render(request, 'services/enseignants.html',{'datetime': timezone.now(), 'Enseignants' : liste_ens})


def liste_ue(request):
	order_by = request.GET.get('order_by', 'année')
	liste_ue = Ue.objects.order_by(order_by)
	return render(request, 'services/ues.html',{'datetime': timezone.now(), 'Ue' : liste_ue})


def liste_taches(request):
	order_by = request.GET.get('order_by', 'ue')
	liste = Tache.objects.all().order_by(order_by)
	return render(request, 'services/taches.html',{'datetime': timezone.now(), 'Taches' : liste})



#-----------------------------------------------
# Affichage un(e) seul(e)


class tache_detail(generic.DetailView):
    model = Tache
    template_name = 'services/tache_detail.html'

    def get_context_data(self, **kwargs):
        context = super(tache_detail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def une_ue(request,pk):
	return render(request, "services/une_ue.html", {'ue': Ue.objects.get(id=pk),'datetime': timezone.now()})

def un_enseignant(request,pk):
	return render(request, "services/un_ens.html", {'ens': Enseignant.objects.filter(id=pk)[0], 'datetime': timezone.now()})


class ue_detail(generic.DetailView):
    model = Ue
    template_name = 'services/ue_detail.html'


def une_ue(request,pk):
	return render(request, "services/une_ue.html", {'ue': Ue.objects.get(id=pk),'datetime': timezone.now()})

def un_enseignant(request,pk):
	return render(request, "services/un_ens.html", {'ens': Enseignant.objects.filter(id=pk)[0], 'datetime': timezone.now()})


#-----------------------------------------------
# Formulaires


def tache_form(request,pk):
	return render(request, "services/tache_form.html", {'datetime': timezone.now()})


def nouvelletache(request):
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = TacheForm(request.POST)  # Nous reprenons les données

		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			form.save()
			return HttpResponseRedirect('enseignants')

	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		form = TacheForm()  # Nous créons un formulaire vide

	return render(request, "services/tache_form.html", {'form':form, 'datetime': timezone.now()})



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

	return render(request, "services/ue_form.html", {'datetime': timezone.now()})







#-----------------------------------------------
# Create
from django.core.urlresolvers import reverse
from django.views.generic import CreateView

class CreateTacheView(CreateView):
    model = Tache
    template_name = 'services/edit_tache.html'
    form_class = TacheForm

    def get_success_url(self):
        return reverse('taches')

    def get_context_data(self, **kwargs):
        context = super(CreateTacheView, self).get_context_data(**kwargs)
        context['action'] = reverse('tache-new')
        context['datetime'] = timezone.now()
        return context

class CreateUeView(CreateView):
    model = Ue
    template_name = 'services/edit_ue.html'
    form_class = UeForm

    def get_success_url(self):
        return reverse('ue_list')

    def get_context_data(self, **kwargs):
        context = super(CreateUeView, self).get_context_data(**kwargs)
        context['action'] = reverse('ue-new')
        context['datetime'] = timezone.now()
        return context

#---------------------
# Edit

from django.views.generic import UpdateView
from services import forms
class UpdateTacheView(UpdateView):

    model = Tache
    template_name = 'edit_tache.html'
    #fields = ('first_name','last_name')
    form_class = forms.TacheForm

    def get_success_url(self):
        return reverse('taches')

    def get_context_data(self, **kwargs):
        context = super(UpdateTacheView, self).get_context_data(**kwargs)
        context['action'] = reverse('tache-edit', kwargs={'pk': self.get_object().id})
        return context


#-----------------------------------------------
# Delete


from django.views.generic import DeleteView
class DeleteTacheView(DeleteView):

    model = Tache
    template_name = 'delete_tache.html'

    def get_success_url(self):
        return reverse('taches')

#-----------------------------------------------
# Detail
       

from django.views.generic import DetailView
class TacheView(DetailView):

    model = Tache
    template_name = 'tache.html'
    exclude = ()


