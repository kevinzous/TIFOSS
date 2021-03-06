from . import views
from django.conf.urls import url
from django.views.generic import TemplateView
# -*- coding: utf-8 -*-

urlpatterns=[
    url(r'^inscription$',views.inscription, name='inscription'),
    url(r'^compteUtilisateur/(\d+)$',views.compteUtilisateur,name='compteUtilisateur'),
    url(r'^ajouterJoueur/(\d+)$',views.ajouterJoueur, name='ajouterJoueur'),
    url(r'^connexion$',views.connexion, name='connexion'),
    url(r'^accesCompte/(\d+)$', views.accesCompte, name='accesCompte'),
    url(r'^deconnexion$',views.deconnexion, name='deconnexion'),
    url(r'^modifierJoueur/(\d+)$',views.modifierJoueur, name='modifierJoueur'),
    ]
