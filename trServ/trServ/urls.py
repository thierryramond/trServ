from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'trServ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'services.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/', 'services.views.home'),
    url(r'^enseignants/', 'services.views.liste_enseignants'),
    url(r'^ue/$', 'services.views.liste_ue'),
    url(r'^taches/', 'services.views.liste_taches'),
    url(r'^nouvelens/', 'services.views.nouvelens'),
    url(r'^nouvelleue/', 'services.views.nouvelleue'),
    url(r'ue/(?P<code>.+$)', 'services.views.une_ue'),
]
