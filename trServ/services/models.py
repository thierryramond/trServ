from django.db import models
from django.db.models import Sum
from django.core.urlresolvers import reverse
from django.utils import timezone

#----------------------------------------------------------------------------------------------
# Listes

nature_tache = (('TD','TD'),('Cours','Cours'),('Intégré','Intégré'),('TP','TP'),)
année = (('00','00'),('L1','L1'),('L2','L2'),('L3','L3'),('M1','M1'),('M2','M2'),('D','D'))
semestre = (('S1','S1'),('S2','S2'),('S3','S3'),('S4','S4'),('S5','S5'),('S6','S6'))

#----------------------------------------------------------------------------------------------
# Table des enseignants

class Enseignant(models.Model):
    nom = models.CharField(max_length = 100)
    prenom = models.CharField(max_length = 100)
    grade = models.CharField(max_length = 100)
    service_du = models.IntegerField (default = 192)
    decharge = models.IntegerField (default = 0)
    commentaire = models.CharField(max_length = 255, blank= True)
    arrivé_en = models.DateField(default='2000-09-01')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')
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
        return (self.service_du-self.decharge-att)

    
    def total_attribué_1(self):
        total = Tache.objects.filter(attribué_à = self).aggregate(Sum('horaire_eqtd'))
        if (total['horaire_eqtd__sum'] == None):
            total['horaire_eqtd__sum']=0
        self.attribué=total['horaire_eqtd__sum']
        return total['horaire_eqtd__sum']

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

    def get_absolute_url(self):
        return reverse('enseignant-view', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.bilan = self.calcul_bilan()
        self.attribue = self.total_attribué_1()
        super(Enseignant, self).save( *args, **kwargs)

#----------------------------------------------------------------------------------------------
# Table des UEs

class Ue(models.Model):
    titre = models.CharField(max_length = 100)
    code = models.CharField(max_length = 20)
    année = models.CharField(max_length = 20, choices = année)
    semestre = models.CharField(max_length = 20, choices = semestre)
    description = models.CharField(max_length = 255, blank=True, null=True)
    responsable = models.ForeignKey(Enseignant)
    spécialité = models.CharField(max_length = 20,blank=True, null=True)
    horaire_total = models.IntegerField(default=0)
    horaire_cours = models.IntegerField(default=0)
    horaire_td = models.IntegerField(default=0)
    horaire_tp = models.IntegerField(default=0)
    horaire_intégré = models.IntegerField(default=0)
    horaire_soutien = models.IntegerField(default=0)
    horaire_coordination = models.IntegerField(default=0)
    nombre_td = models.IntegerField(default=0)
    nombre_tp = models.IntegerField(default=0)
    nombre_cours = models.IntegerField(default=0)
    nombre_intégré = models.IntegerField(default=0)
    nombre_soutien = models.IntegerField(default=0)
    millesime = models.IntegerField(default=timezone.now().year)

    def __str__(self):
        return ('{0} - {1}'.format(self.code, self.titre))

    def get_absolute_url(self):
        return reverse('ue-view', kwargs={'pk': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


    class Meta():
        unique_together = ( 'code', 'millesime')



#----------------------------------------------------------------------------------------------
# Table des taches


class Tache(models.Model):
    ue = models.ForeignKey(Ue)
    attribué_à = models.ForeignKey(Enseignant)
    nature = models.CharField(max_length = 20, choices = nature_tache)
    horaire_reel = models.IntegerField()
    horaire_eqtd = models.FloatField(blank = True, null = True)
    modifié_le = models. DateTimeField(auto_now = True)
    depuis = models.IntegerField(default=0)
    millesime = models.IntegerField(default=timezone.now().year)

    def calcul_eqtd(self):
        if self.nature == 'Intégré': self.horaire_eqtd = self.horaire_reel*1.25
        elif self.nature == 'Cours': self.horaire_eqtd = self.horaire_reel*1.5
        else :  self.horaire_eqtd = self.horaire_reel
        return self.horaire_eqtd


    
    def __str__(self):
        return ('{0} - {1}'.format(self.ue,  self.nature))

    def save(self, *args,**kwargs):
        # Mise a jour de l'enseignant concerné
        self.horaire_eqtd = self.calcul_eqtd()
        self.attribué_à.attribué= self.attribué_à.total_attribué_1()
        self.attribué_à.bilan = self.attribué_à.calcul_bilan()
        self.attribué_à.save()
        # Mise à jour de l'UE concernée
        # a faire
        super(Tache,self).save( *args, **kwargs)

