from django.db import models

# Create your models here.

class Enseignant(models.Model):
	nom = models.CharField(max_length = 100)
	prenom = models.CharField(max_length = 100)
	grade = models.CharField(max_length = 100)
	service_du = models.IntegerField (default = 192)
	decharge = models.IntegerField (default = 0)
	commentaire = models.TextField
	arrivé_en = models.DateField
	photo = models.ImageField
	attribué = models.IntegerField (default = 0)

	def __str__(self):
		return ('{0}, {1}'.format(self.nom, self.prenom))


class Ue(models.Model):
	titre = models.CharField(max_length = 100)
	code = models.CharField(max_length = 20)
	année = models.CharField(max_length = 20)
	semestre = models.CharField(max_length = 20)
	description = models.TextField
	responsable = models.ForeignKey(Enseignant)
	specialité = models.CharField(max_length = 20)

	def __str__(self):
		return ('{0}, {1}'.format(self.code, self.titre))


class Tache(models.Model):
	ue = models.ForeignKey(Ue)
	enseignant = models.ForeignKey(Enseignant)
	nature = models.CharField(max_length = 20)
	horaire_reel = models.IntegerField 
	horaire_eqtd = models.IntegerField
	modifié_le = models. DateTimeField(auto_now = True)
	
	def __str__(self):
		return ('{0}, {1}'.format(self.ue, self.nature))
