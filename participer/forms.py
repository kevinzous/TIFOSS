from django import forms
from .models import joueur
from django.contrib.auth.models import User

class connexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


    
class inscriptionForm(forms.Form):
    nom=forms.CharField(label="Nom d'utilisateur",max_length=30)
    prenom=forms.CharField(label='Ton prénom',max_length=30)
    email=forms.EmailField(label='Mail')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def clean_nom(self):
        name=self.cleaned_data['nom']
        ListeUser=User.objects.filter(username=name)
        x=ListeUser.count()
        if x != 0:
            raise forms.ValidationError("Nom d'utilisateur déjà utilisé")
        return name
        

class compteUtilisateurForm(forms.Form):
    nomEquipe=forms.CharField(label="Nom de l'équipe", max_length=50)
    nomEcole=forms.CharField(label="Nom de l'école", max_length=50)

           
class joueurForm(forms.ModelForm):
    hébérgement=forms.BooleanField(required=False)
    repas_Samedi=forms.BooleanField(required=False)
    repas_Dimanche=forms.BooleanField(required=False)
    soirée=forms.BooleanField(required=False)
    nom=forms.CharField(max_length=50)
    prénom=forms.CharField(max_length=50)
#    SIZE_SHIRTS=(('S','taille S'),('M','taille M'),('L','taille L'),('XL','taille XL'))
#    SEXE=(('M','Masculin'),('F','Feminin'))
    class Meta:
        model=joueur
        fields = ('taille','sexe')
    
    
    
    

    
