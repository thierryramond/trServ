from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView

from .models import Enseignant, Tache, Ue
from .forms import EnseignantForm, UeForm, TacheForm
from services import forms



#-------------------------------------------------------------------------------------------
# acceuil
#-------------------------------------------------------------------------------------------


def home(request):
	return render(request,'home.html',{'datetime': timezone.now()})


#-------------------------------------------------------------------------------------------
# Taches
#-------------------------------------------------------------------------------------------


# Affichage par liste

def liste_taches(request):
    order_by = request.GET.get('order_by', 'ue')
    liste = Tache.objects.all().order_by(order_by)
    return render(request, 'taches.html',{'datetime': timezone.now(), 'Taches' : liste})

# Affichage d'une tache 

class TacheView(DetailView):

    model = Tache
    template_name = 'tache.html'
    exclude = ()



class tache_detail(generic.DetailView):
    model = Tache
    template_name = 'tache_detail.html'

    def get_context_data(self, **kwargs):
        context = super(tache_detail, self).get_context_data(**kwargs)
        context['timezone'] = timezone.now()
        return context

# Creation d'une tache

class CreateTacheView(CreateView):
    model = Tache
    template_name = 'edit_tache.html'
    form_class = TacheForm

    def get_success_url(self):
        return reverse('taches')

    def get_context_data(self, **kwargs):
        context = super(CreateTacheView, self).get_context_data(**kwargs)
        context['action'] = reverse('tache-new')
        context['datetime'] = timezone.now()
        return context


# Mise à jour d'une tache

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


# Effacer une tache

from django.views.generic import DeleteView
class DeleteTacheView(DeleteView):

    model = Tache
    template_name = 'tache_delete.html'

    def get_success_url(self):
        return reverse('taches')


# Formulaire tache


def tache_form(request,pk):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = TacheForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()
            return HttpResponseRedirect('taches',{'datetime': timezone.now()})

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = TacheForm()  # Nous créons un formulaire vide

    return render(request, "tache_form.html", {'form':form, 'datetime': timezone.now()})



#-------------------------------------------------------------------------------------------
# UEs
#-------------------------------------------------------------------------------------------

# Affichage par liste

def liste_ue(request):
    order_by = request.GET.get('order_by', 'année')
    liste_ue = Ue.objects.order_by(order_by)
    return render(request, 'ues.html',{'datetime': timezone.now(), 'Ue' : liste_ue})

# Affichage une UE

def une_ue(request,pk):
    return render(request, "une_ue.html", {'ue': Ue.objects.get(id=pk),'datetime': timezone.now()})


class ue_detail(generic.DetailView):
    model = Ue
    template_name = 'ue_detail.html'

# Creation UE


class CreateUeView(CreateView):
    model = Ue
    template_name = 'edit_ue.html'
    form_class = UeForm
    

    def get_success_url(self):
        return reverse('ues')

    def get_context_data(self, **kwargs):
        context = super(CreateUeView, self).get_context_data(**kwargs)
        context['action'] = reverse('ue-new')
        context['datetime'] = timezone.now()
        return context


def nouvelleue(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = UeForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = UeForm()  # Nous créons un formulaire vide

    return render(request, "ue_form.html", {'datetime': timezone.now()})


# Mise à jour UE


class UpdateUeView(UpdateView):

    model = Ue
    template_name = 'edit_ue.html'
    #fields = ('first_name','last_name')
    form_class = forms.UeForm

    def get_success_url(self):
        return reverse('ues')

    def get_context_data(self, **kwargs):
        context = super(UpdateUeView, self).get_context_data(**kwargs)
        context['action'] = reverse('ue-edit', kwargs={'pk': self.get_object().id})
        return context




# Effacer UE

class DeleteUeView(DeleteView):

    model = Ue
    template_name = 'ue_delete.html'

    def get_success_url(self):
        return reverse('ues')


# Formulaire UE

def ue_form(request,pk):

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = UeForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()
            return HttpResponseRedirect('ue',{'datetime': timezone.now()})

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = UeForm()  # Nous créons un formulaire vide

    return render(request, "ue_form.html", {'form':form, 'datetime': timezone.now()})



#-----------------------------------------------
# Enseignants
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
	return render(request, 'enseignants.html',{'datetime': timezone.now(), 'Enseignants' : liste_ens})



# Affichage un enseignant

def un_enseignant(request,pk):
    return render(request, "un_ens.html", {'ens': Enseignant.objects.filter(id=pk)[0], 'datetime': timezone.now()})

# Creer un enseignant


class CreateEnseignantView(CreateView):
    model = Enseignant
    template_name = 'edit_enseignant.html'
    form_class = EnseignantForm

    def get_success_url(self):
        return reverse('enseignants')

    def get_context_data(self, **kwargs):
        context = super(CreateEnseignantView, self).get_context_data(**kwargs)
        context['action'] = reverse('enseignant-new')
        context['datetime'] = timezone.now()
        return context


def nouvelens(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = EnseignantForm(request.POST)  # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            form.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = EnseignantForm()  # Nous créons un formulaire vide

    return render(request, "ens_form.html",{'datetime': timezone.now()})


# Mise à jour enseignant


class UpdateEnseignantView(UpdateView):

    model = Enseignant
    template_name = 'edit_enseignant.html'
    form_class = forms.EnseignantForm

    def get_success_url(self):
        return reverse('enseignants')

    def get_context_data(self, **kwargs):
        context = super(UpdateEnseignantView, self).get_context_data(**kwargs)
        context['action'] = reverse('enseignant-edit', kwargs={'pk': self.get_object().id})
        return context

# Effacer un enseignant

class DeleteEnseignantView(DeleteView):

    model = Enseignant
    template_name = 'enseignant_delete.html'

    def get_success_url(self):
        return reverse('enseignants')


# formulaire enseignant

def ens_form(request,pk):
    return render(request, "ens_form.html", {'ens': Enseignant.objects.get(id=pk) , 'datetime': timezone.now()})





#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------






#-----------------------------------------------





















