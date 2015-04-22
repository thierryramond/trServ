from django.conf.urls import url
from . import views
from .models import Tache


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index', views.home, name='home'),
    url(r'^accueil/', views.home, name='home'),
    url(r'^enseignants/$', views.liste_enseignants, name ='enseignants'),
    url(r'^enseignant/(?P<pk>\d+$)', views.un_enseignant, name='enseignant'),
    url(r'^ue/$', views.liste_ue, name='ue'),
    url(r'^taches/$', views.liste_taches, name='taches'),
    url(r'^tache/(?P<pk>\d+$)$', views.tache_detail.as_view(),name='tache-view'),
    url(r'^tache_form/$', views.nouvelletache,  name= 'tache_form'),
    url(r'ue/(?P<pk>.+$)', views.une_ue, name ='une_ue'),
    url(r'^filter$', views.CreateTacheView.as_view(), name='tache-filter'),
    url(r'^new$', views.CreateTacheView.as_view(), name='tache-new'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateTacheView.as_view(), name='tache-edit',),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteTacheView.as_view(), name='tache-delete',),
    url(r'^(?P<pk>\d+)/$', views.Tache, name='tache-view',),
    ]