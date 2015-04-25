from django.conf.urls import url
from . import views
from .models import Tache


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^index', views.home, name='home'),
    url(r'^accueil/', views.home, name='home'),

    url(r'^enseignants/$', views.liste_enseignants, name ='enseignants'),
    url(r'^enseignant/(?P<pk>\d+)$', views.un_enseignant, name='enseignant-view'),
    url(r'^enseignant/new$', views.CreateEnseignantView.as_view(), name='enseignant-new'),
    url(r'^enseignant/update/(?P<pk>\d+)$', views.UpdateEnseignantView.as_view(), name='enseignant-edit'),
    url(r'^enseignant/delete/(?P<pk>\d+)$', views.DeleteEnseignantView.as_view(), name='enseignant-delete'),
    
    url(r'^taches/$', views.liste_taches, name='taches'),
    url(r'^tache/(?P<pk>\d+$)$', views.TacheDetailView.as_view(),name='tache-view'),
    url(r'^tache_form/$', views.tache_form,  name= 'tache_form'),
    url(r'^tache/filter$', views.CreateTacheView.as_view(), name='tache-filter'),
    url(r'^tache/new$', views.CreateTacheView.as_view(), name='tache-new'),
    url(r'^tache/edit/(?P<pk>\d+)/$', views.UpdateTacheView.as_view(), name='tache-edit',),
    url(r'^tache/delete/(?P<pk>\d+)/$', views.DeleteTacheView.as_view(), name='tache-delete',),

    url(r'^ues/$', views.liste_ue, name='ues'),
    url(r'^ue/(?P<pk>.+$)', views.UpdateUeView.as_view(), name ='ue-edit'),
    url(r'^ue_new/$', views.CreateUeView.as_view(), name='ue-new'),

    ]