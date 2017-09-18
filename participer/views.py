from django.shortcuts import render
from .forms import inscriptionForm, compteUtilisateurForm, joueurForm, connexionForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import equipe, joueur,forfait
from django.http import HttpResponse
# -*- coding: utf-8 -*-

def accueil(request):
    equipes=equipe.objects.filter(paye=True)
    equipes=list(equipes)

    return render(request, 'informations/pageAccueil.html',locals())


def connexion(request):
    form=connexionForm(request.POST or None)
    success=False
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
        else:
            error = True
        success=True
        
    return render(request,'participer/connexion.html', locals())

def deconnexion(request):
    logout(request)
    equipes=equipe.objects.filter(paye=True)
    equipes=list(equipes)
    return render(request, 'informations/pageAccueil.html', locals())


def accesCompte(request, id_u):
     nomEquipe=equipe.objects.get(identifiant=id_u).nom
     nomEcole=equipe.objects.get(identifiant=id_u).ecole
     equipe2=equipe.objects.get(identifiant=id_u)
     joueurs=joueur.objects.filter(team=equipe2)
     joueurs=list(joueurs)
     n=0
     for J in joueurs:
         if J.paye==True:
             n+=1
     etatEquipe=''
     if n>=5:
         etatEquipe='Equipe inscrite'
         equipe2.paye=True
     else:
         etatEquipe="L'equipe doit contenir au moins 5 joueurs dont le paiement a ete valide par l'organisation pour etre definitivement inscrite au tournoi"
         equipe2.paye=False
         
     success1=True

     return render(request, 'participer/constitutionEquipe.html', locals())
    

def inscription(request):
    form=inscriptionForm(request.POST or None)
    success=False
    if form.is_valid():
        nom=form.cleaned_data['nom']
        prenom=form.cleaned_data['prenom']
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        success=True
        user = User.objects.create_user(nom,email,password)
        login(request, user)
        user.save()
        identifiant=user.id
        user.save()    
        
    

    return render(request, 'participer/inscription.html', locals())


@login_required
def compteUtilisateur(request, ident):
    form=compteUtilisateurForm(request.POST or None)
    succes=False
    if form.is_valid():
        nomEquipe=form.cleaned_data['nomEquipe']
        nomEcole=form.cleaned_data['nomEcole']
        team=equipe(nom=nomEquipe, ecole=nomEcole,identifiant=ident,paye=False)
        team.id=ident
        equipeIdentifiant=ident
        succes=True
        team.save()
    return render(request,'participer/compteUtilisateur.html',locals())

@login_required
def ajouterJoueur(request, id_equipe):
    form=joueurForm(request.POST or None)
    success1=False
    if form.is_valid():
        hebergement=form.cleaned_data['hébérgement']
        repas_Samedi=form.cleaned_data['repas_Samedi']
        repas_Dimanche=form.cleaned_data['repas_Dimanche']
        soirée=form.cleaned_data['soirée']
        forfaitJ=forfait(hebergement=hébérgement, repasSamedi=repas_Samedi, repasDimanche=repas_Dimanche, soiree=soirée)
        forfaitJ.save()
        nom=form.cleaned_data['nom']
        prénom=form.cleaned_data['prénom']
        taille=form.cleaned_data['taille']
        sexe=form.cleaned_data['sexe']
        
        joueur2=joueur(nom=nom,prenom=prénom,taille=taille, forfait=forfaitJ, sexe=sexe,team=equipe.objects.get(identifiant=id_equipe),paye=False)
        
        equipe2=equipe.objects.get(identifiant=id_equipe)
        nomEquipe=equipe2.nom
        nomEcole=equipe2.ecole
        reglement=equipe2.paye
        joueur2.save()
        
        joueurs=joueur.objects.filter(team=equipe2)
        joueurs=list(joueurs)
        n=0
        for J in joueurs:
            if J.paye==True:
                n+=1
        etatEquipe=''
        if n>=5:
            etatEquipe='Equipe inscrite'
            equipe2.paye=True
        else:
            etatEquipe="L'equipe doit contenir au moins 5 joueurs dont le paiement a ete valide par l'organisation pour etre definitivement inscrite au tournoi"
            equipe2.paye=False
         
        success1=True

    return render(request, 'participer/constitutionEquipe.html', locals())

@login_required
def modifierJoueur(request,id_joueur):
    form=joueurForm(request.POST or None)
    succes=False
    if form.is_valid():
        J=joueur.objects.get(id=id_joueur)#On supprime le joueur avec les infos erronnees et on recupere l equipe a laquelle il appartenait 
        equipe1=J.team       
        J.delete()
        
        hebergement=form.cleaned_data['hébérgement']#On recupere les infos du formulaire et on cree un nouveau forfait
        repasSamedi=form.cleaned_data['repas_Samedi']
        repasDimanche=form.cleaned_data['repas_Dimanche']
        soiree=form.cleaned_data['soirée']
        forfaitJ=forfait(hebergement=hebergement, repasSamedi=repasSamedi, repasDimanche=repasDimanche, soiree=soiree)
        forfaitJ.save()
        nom=form.cleaned_data['nom']
        prenom=form.cleaned_data['prénom']
        taille=form.cleaned_data['taille']
        sexe=form.cleaned_data['sexe']
        
        joueur2=joueur(nom=nom,prenom=prénom,taille=taille, forfait=forfaitJ, sexe=sexe,team=equipe1,paye=False)
                                                                          
        nomEquipe=equipe1.nom
        nomEcole=equipe1.ecole
        joueur2.save()
        
        joueurs=joueur.objects.filter(team=equipe1)
        joueurs=list(joueurs)
        n=0
        for J in joueurs:
            if J.paye==True:
                n+=1
        etatEquipe=''
        if n>=5:
            etatEquipe='Equipe inscrite'
            equipe1.paye=True
        else:
            etatEquipe="L'equipe doit contenir au moins 5 joueurs dont le paiement a ete valide par l'organisation pour etre definitivement inscrite au tournoi"
            equipe1.paye=False
         
        id_equipe=equipe1.identifiant
        success1=True

    return render(request, 'participer/constitutionEquipe.html', locals())
        
        
    
    
