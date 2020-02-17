# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# -------------------La table Etudiants--------------------

class Etudiants(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=30)
    classe = models.CharField(max_length=15)
    genie = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    photo = models.ImageField()
    genre = models.CharField(max_length=15)

# -------------------La table Documents--------------------

class Documents(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    classe = models.CharField(max_length=15)
    genie = models.CharField(max_length=15)
    matiere = models.CharField(max_length=15)
    objet = models.CharField(max_length=15)

# -------------------La table Publications--------------------

class Publications(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE )

# -------------------La table Consultations--------------------

class Consultations(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    document = models.ForeignKey(Documents, on_delete=models.CASCADE)
