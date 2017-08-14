from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# -*- coding: utf-8 -*-

class joueur(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    SIZE_SHIRTS=(('S','taille S'),('M','taille M'),('L','taille L'),('XL','taille XL'))
    taille=models.CharField(max_length=2, choices=SIZE_SHIRTS,default='S')
    forfait=models.ForeignKey('forfait')
    SEXE=(('M','Masculin'),('F','Feminin'))
    sexe=models.CharField(max_length=1, choices=SEXE)
    ecole=models.CharField(max_length=50)
    team=models.ForeignKey('equipe')
    paye=models.BooleanField()
    def __str__(self):
        return '{0} {1}'.format(self.prenom, self.nom)
        

class forfait(models.Model):
    hebergement=models.BooleanField()
    repasSamedi=models.BooleanField()
    repasDimanche=models.BooleanField()
    soiree=models.BooleanField()    
    l=''
    somme=25
    
        
    def __str__(self):
        if self.hebergement:
            self.l+=' hebergement+'
            self.somme+=3
        if self.repasSamedi:
            self.l+=' repas du samedi +'
            self.somme+=2
        if self.repasDimanche:
            self.l+=' repas du dimanche +'
            self.somme+=2
        if self.soiree:
            self.l+=' Soiree'
            self.somme+=5
        return 'tournoi +{0}     Somme a payer: {1}'.format(self.l,self.somme)
        
        
        

class equipe(models.Model):
    nom=models.CharField(max_length=80)
    ecole=models.CharField(max_length=50)
    joueurs=models.ManyToManyField('joueur')
    identifiant=models.IntegerField()
    paye=models.BooleanField()

    def __str__(self):
        return self.nom

    
    
    
