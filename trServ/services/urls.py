from django.conf.urls import url
from . import views
from .models import Tache


urlpatterns = [
    url(r'^$', views.home),
    url(r'^index', views.home),
    url(r'^accueil/', views.home),
    url(r'^enseignants/$', views.liste_enseignants, name ='enseignants'),
    url(r'^enseignant/(?P<pk>\d+$)', views.un_enseignant, name='enseignant'),
    url(r'^ue/$', views.liste_ue, name='ue'),
    url(r'^taches/$', views.liste_taches, name='taches'),
    url(r'^tache/(?P<pk>\d+$)$', views.tache_detail.as_view(),name='tache'),
    url(r'ue/(?P<pk>.+$)', views.une_ue, name ='une_ue'),
    ]