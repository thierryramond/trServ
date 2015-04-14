from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView
from services.models import Enseignant

urlpatterns = [
    # Examples:
    # url(r'^$', 'trServ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'services.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/', 'services.views.home'),
    url(r'^enseignants/$', 'services.views.liste_enseignants'),
    url(r'^ue/$', 'services.views.liste_ue'),
    url(r'^taches/', 'services.views.liste_taches'),
    url(r'^nouvelens/', 'services.views.nouvelens'),
    url(r'^nouvelleue/', 'services.views.nouvelleue'),
    url(r'ue/(?P<code>.+$)', 'services.views.une_ue'),
    url(r'^liste$', ListView.as_view(model=Enseignant,)),
    url(r'^enseignants/(?P<pk>\d+$)', 'services.views.un_enseignant'),
    url(r'^ens/(?P<pk>\d+$)', 'services.views.ens_form'),
]
