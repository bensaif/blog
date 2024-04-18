from django.db import models

from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Import différé pour éviter les importations circulaires
# Importez ce dont vous avez besoin uniquement lors de son utilisation

class SalleForm(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nom')
    etablissement = models.CharField(max_length=100, verbose_name='Etablissement')
    date_arrivee = models.DateField(verbose_name='Date au')
    date_depart = models.DateField(verbose_name='Date du')
    nom_salle_souhaite = models.CharField(max_length=100, verbose_name='Nom de la salle souhaitée')
    nombre_personnes = models.IntegerField(verbose_name='Nombre de personnes')
    type_evenement = models.CharField(max_length=100, verbose_name='Type d\'événement')
    pause_cafe = models.IntegerField(verbose_name='Pause café')
    dejeuner = models.IntegerField(verbose_name='Déjeuner')
    diner = models.IntegerField(verbose_name='Dîner')
    nombre_courrier = models.IntegerField(verbose_name='Nombre de courrier')
    moyen = models.CharField(max_length=100, verbose_name='Moyen')
    statue = models.CharField(max_length=100, verbose_name='Statut')
    commentaire = models.CharField(max_length=255, blank=True, verbose_name='Commentaire')

class HebergementForm(models.Model):
    nombre_courrier = models.IntegerField(verbose_name='Nombre de courrier')
    etablissement = models.CharField(max_length=100, verbose_name='Etablissement')
    demandeur = models.CharField(max_length=100, verbose_name='Demandeur')
    capacite = models.IntegerField(verbose_name='Capacité')
    date_arrivee = models.DateField(verbose_name='Date au')
    date_depart = models.DateField(verbose_name='Date du')
    chambre_disponible = models.CharField(max_length=100, verbose_name='Chambre disponible')
    prise_charge = models.CharField(max_length=100, verbose_name='Prise en charge')
    nombre_personnes = models.IntegerField(verbose_name='Nombre de personnes')
    moyen = models.CharField(max_length=100, verbose_name='Moyen')
    statue = models.CharField(max_length=100, verbose_name='Statut')
    type = models.TextField(blank=True, verbose_name='Type')

class Salle_heberForm(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nom')
    etablissement = models.CharField(max_length=100, verbose_name='Etablissement')
    date_arrivee = models.DateField(verbose_name='Date au')
    date_depart = models.DateField(verbose_name='Date du')
    nom_salle_souhaite = models.CharField(max_length=100, verbose_name='Nom de la salle souhaitée')
    nombre_personnes = models.IntegerField(verbose_name='Nombre de personnes')
    type_evenement = models.CharField(max_length=100, verbose_name='Type d\'événement')
    pause_cafe = models.IntegerField(verbose_name='Pause café')
    dejeuner = models.IntegerField(verbose_name='Déjeuner')
    diner = models.IntegerField(verbose_name='Dîner')
    nombre_courrier = models.IntegerField(verbose_name='Nombre de courrier')
    moyen = models.CharField(max_length=100, verbose_name='Moyen')
    statue = models.CharField(max_length=100, verbose_name='Statut')
    commentaire = models.TextField(blank=True, verbose_name='Commentaire')


class Event(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nom de l\'événement')
    date = models.DateField(verbose_name='Date de l\'événement')
    lieu = models.CharField(max_length=100, verbose_name='Lieu de l\'événement', default='Emplacement inconnu')

    def __str__(self):
        return f"{self.nom} ({self.date}) - Lieu : {self.lieu}"

