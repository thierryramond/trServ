from django.contrib import admin

# Register your models here.

from .models import Enseignant, Tache, Ue

admin.site.register(Enseignant)
admin.site.register(Tache)
admin.site.register(Ue)
