from django import forms
from .models import joueur
from django.contrib.auth.models import User

class connexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


    
class inscriptionForm(forms.Form):
    nom=forms.CharField(label="Nom d'utilisateur",max_length=30)
    prenom=forms.CharField(label='Ton prenom',max_length=30)
    email=forms.EmailField(label='Mail')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def clean_nom(self):
        name=self.cleaned_data['nom']
        ListeUser=User.objects.filter(username=name)
        x=ListeUser.count()
        if x != 0:
            raise forms.ValidationError("Nom d'utilisateur deja utilise")
        return name
        

class compteUtilisateurForm(forms.Form):
    nomEquipe=forms.CharField(label="Nom de l'equipe", max_length=50)
    nomEcole=forms.CharField(label="Nom de l'ecole", max_length=50)

           
class joueurForm(forms.ModelForm):
    hebergement=forms.BooleanField(required=False)
    repasSamedi=forms.BooleanField(required=False)
    repasDimanche=forms.BooleanField(required=False)
    soiree=forms.BooleanField(required=False)
    nom=forms.CharField(max_length=50)
    prenom=forms.CharField(max_length=50)
#    SIZE_SHIRTS=(('S','taille S'),('M','taille M'),('L','taille L'),('XL','taille XL'))
#    SEXE=(('M','Masculin'),('F','Feminin'))
    class Meta:
        model=joueur
        fields = ('taille','sexe')
    
    
    
    

    
