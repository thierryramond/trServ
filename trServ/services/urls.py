from django.conf.urls import url

urlpatterns = [
    url(r'^enseignants/', 'services.views.liste_enseignants'),
    url(r'^ue/', 'services.views.liste_ue'),
    url(r'^taches/', 'services.views.liste_taches'),
    url(r'^nouvelens/', 'services.views.nouvelens'),
    url(r'^nouvelleue/', 'services.views.nouvelleue'),
    ]