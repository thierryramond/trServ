from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView,FormView

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
    return render(request, 'tache_list.html',{'datetime': timezone.now(), 'Taches' : liste})

# Affichage d'une tache 

class TacheDetailView(generic.DetailView):

    model = Tache
    template_name = 'tache_detail.html'
    exclude = ()

    def get_context_data(self, **kwargs):
        context = super(TacheDetailView, self).get_context_data(**kwargs)
        context['datetime'] = timezone.now()
        return context

# Creation d'une tache

class CreateTacheView(CreateView):
    model = Tache
    template_name = 'tache_edit.html'
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
    template_name = 'tache_edit.html'
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
    return render(request, 'ue_list.html',{'datetime': timezone.now(), 'Ue' : liste_ue})

# Affichage une UE

class UeDetailView(generic.DetailView):

    model = Ue
    template_name = 'ue_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UeDetailView, self).get_context_data(**kwargs)
        context['datetime'] = timezone.now()
        return context

    
# Creation UE


class CreateUeView(CreateView):
    model = Ue
    template_name = 'ue_edit.html'
    form_class = forms.UeForm

    


    def get_success_url(self):
        return reverse('ues')

    def get_context_data(self, **kwargs):
        context = super(CreateUeView, self).get_context_data(**kwargs)
        context['action'] = reverse('ue-new')
        context['datetime'] = timezone.now()
        return context


# Mise à jour UE


class UpdateUeView(UpdateView):

    model = Ue
    template_name = 'ue_edit.html'
    form_class = forms.UeForm

    def get_success_url(self):
        return reverse('ues')

    def get_context_data(self, **kwargs):
        context = super(UpdateUeView, self).get_context_data(**kwargs)
        context['action'] = reverse('ue-edit', kwargs={'pk': self.get_object().id})
        context['datetime'] = timezone.now()
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
    template_name= 'enseignant_list.html'

    def get_context_data(self, **kwargs):
        context = super(EnseignantListView, self).get_context_data(**kwargs)
        context['datetime'] = timezone.now()
        return context

    def get_queryset(self):
        if self.request.GET.get('sort_by'):
            sort_by = self.request.GET.get('sort_by')
            qs = super(EnseignantListView, self).get_queryset().order_by(sort_by)
        else:
            qs = super(EnseignantListView, self).get_queryset()
        
        if self.request.GET.get('order'):
            order = self.request.GET.get('order')
            if order == 'desc': qs = qs.reverse()
        return qs


def liste_enseignants(request):
	order_by = request.GET.get('order_by', 'bilan')
	liste_ens = Enseignant.objects.order_by(order_by)
	return render(request, 'enseignant1_list.html',{'datetime': timezone.now(), 'Enseignants' : liste_ens})



# Affichage un enseignant

def un_enseignant(request,pk):
    return render(request, "un_ens.html", {'enseignant': Enseignant.objects.get(id=pk), 'datetime': timezone.now()})

class EnseignantDetailView(UpdateView):
    model = Enseignant
    template_name = 'enseignant_detail.html'
    form_class = EnseignantForm


    def get_context_data(self, **kwargs):
        context = super(EnseignantDetailView, self).get_context_data(**kwargs)
        context['datetime'] = timezone.now()
        return context

# Creer un enseignant


class CreateEnseignantView(CreateView):
    model = Enseignant
    template_name = 'enseignant_edit.html'
    form_class = EnseignantForm

    def get_success_url(self):
        return reverse('enseignants')

    def get_context_data(self, **kwargs):
        context = super(CreateEnseignantView, self).get_context_data(**kwargs)
        context['action'] = reverse('enseignant-new')
        context['datetime'] = timezone.now()
        return context


# Mise à jour enseignant


class UpdateEnseignantView(UpdateView):

    model = Enseignant
    template_name = 'enseignant_edit.html'
    form_class = forms.EnseignantForm

    def get_success_url(self):
        return reverse('enseignants')

    def get_context_data(self, **kwargs):
        context = super(UpdateEnseignantView, self).get_context_data(**kwargs)
        context['action'] = reverse('enseignant-edit', kwargs={'pk': self.get_object().id})
        context['datetime'] = timezone.now()
        return context

# Effacer un enseignant

class DeleteEnseignantView(DeleteView):

    model = Enseignant
    template_name = 'enseignant_delete.html'

    def get_success_url(self):
        return reverse('enseignants')




#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

