from django.db import models

# Create your models here.

class Enseignant(models.Model):
	nom = models.CharField(max_length = 100)
	prenom = models.CharField(max_length = 100)
	grade = models.CharField(max_length = 100)
	service_du = models.IntegerField (default = 192)
	decharge = models.IntegerField (default = 0)
	commentaire = models.TextField(blank=True)
	arrivé_en = models.DateField()
	photo = models.ImageField(blank=True)
	attribué = models.IntegerField (default = 0)
	bilan = models.IntegerField ()

	def __str__(self):
		return ('{1} {0}'.format(self.nom, self.prenom))


class Ue(models.Model):
	titre = models.CharField(max_length = 100)
	code = models.CharField(max_length = 20)
	année = models.CharField(max_length = 20)
	semestre = models.CharField(max_length = 20)
	description = models.TextField
	responsable = models.ForeignKey(Enseignant)
	specialité = models.CharField(max_length = 20)
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

	def __str__(self):
		return ('{0} - {1}'.format(self.code, self.titre))


class Tache(models.Model):
	ue = models.ForeignKey(Ue)
	attribué_à = models.ForeignKey(Enseignant)
	nature = models.CharField(max_length = 20)
	horaire_reel = models.IntegerField()
	horaire_eqtd = models.IntegerField()
	modifié_le = models. DateTimeField(auto_now = True)
	
	def __str__(self):
		return ('{0} - {1}'.format(self.ue,  self.nature))
