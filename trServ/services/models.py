from django.db import models
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.utils import timezone


# Create your models here.

class Enseignant(models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    grade = models.CharField(max_length = 100)
    service_du = models.IntegerField (default = 192)
    decharge = models.IntegerField (default = 0)
    commentaire = models.CharField(max_length = 255, blank= True)
    arrivé_en = models.DateField(default='2000-09-01')
    photo = models.ImageField(blank=True)
    attribué = models.IntegerField (default = 0)
    bilan = models.IntegerField (default = 0)
    millesime = models.IntegerField (default = timezone.now().year)

    class Meta():
        unique_together = ("nom", "prenom", "millesime")

    def __str__(self):
        return ('{1} {0}'.format(self.nom, self.prenom))


    def calcul_bilan(self):
        att=Tache.objects.filter(attribué_à = self).aggregate(Sum('horaire_eqtd'))['horaire_eqtd__sum']
        if att == None:
            att=0
        self.bilan = self.service_du-self.decharge-att
        self.save()
        return (self.service_du-self.decharge-att)

    
    def total_attribue_1(self):
        total = Tache.objects.filter(attribué_à = self).aggregate(Sum('horaire_eqtd'))
        if (total['horaire_eqtd__sum'] == None):
            total['horaire_eqtd__sum']=0
        self.total_attribue=total['horaire_eqtd__sum']
        self.save()
        return total['horaire_eqtd__sum']

    def get_absolute_url(self):
        return reverse('enseignant-view', kwargs={'pk': self.id})
    

class Ue(models.Model):
    titre = models.CharField(max_length = 100)
    code = models.CharField(max_length = 20)
    année = models.CharField(max_length = 20)
    semestre = models.CharField(max_length = 20)
    description = models.CharField(max_length = 255)
    responsable = models.ForeignKey(Enseignant)
    spécialité = models.CharField(max_length = 20)
    horaire_total = models.IntegerField()
    horaire_cours = models.IntegerField()
    horaire_td = models.IntegerField()
    horaire_tp = models.IntegerField()
    horaire_intégré = models.IntegerField()
    horaire_soutien = models.IntegerField()
    horaire_coordination = models.IntegerField()
    nombre_td = models.IntegerField()
    nombre_tp = models.IntegerField()
    nombre_cours = models.IntegerField()
    nombre_intégré = models.IntegerField()
    nombre_soutien = models.IntegerField()
    millesime = models.IntegerField()

    def __str__(self):
        return ('{0} - {1}'.format(self.code, self.titre))

    def get_absolute_url(self):
        return reverse('ue-view', kwargs={'pk': self.id})

    class Meta():
        unique_together = ( 'code', 'millesime')


nature_tache = (('TD','TD'),('Cours','Cours'),('Intégré','Intégré'),('TP','TP'),)


class Tache(models.Model):
    ue = models.ForeignKey(Ue)
    attribué_à = models.ForeignKey(Enseignant)
    nature = models.CharField(max_length = 20, choices = nature_tache)
    horaire_reel = models.IntegerField()
    horaire_eqtd = models.IntegerField(blank = True, null = True)
    modifié_le = models. DateTimeField(auto_now = True)
    depuis = models.IntegerField(default=0)
    millesime = models.IntegerField(default=timezone.now().year)

    def calcul_eqtd(self):
        if self.nature == 'Intégré': self.horaire_eqtd = self.horaire_reel*1.25
        elif self.nature == 'Cours': self.horaire_eqtd = self.horaire_reel*1.5
        else :  self.horaire_eqtd = self.horaire_reel
        self.save()
        return self.horaire_eqtd


    
    def __str__(self):
        return ('{0} - {1}'.format(self.ue,  self.nature))
