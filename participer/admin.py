from django.contrib import admin
from .models import joueur, equipe, forfait


class joueurAdmin(admin.ModelAdmin):

   list_display   = ('nom', 'prenom','ecole','team', 'taille','forfait', 'sexe')

   list_filter    = ('ecole','team','nom','prenom')

   search_fields  = ('ecole', 'team','nom','prenom')



class equipeAdmin(admin.ModelAdmin):

   list_display   = ('nom','ecole','paye','afficher_joueurs')

   list_filter    = ('ecole','nom','paye')

   search_fields  = ('ecole', 'nom')

   """def afficher_joueurs(self,equipe):
      
                Retourne la liste des joueurs de l'équipe
        
        
        L=equipe.joueurs.all()
        
        M=L.values_list('nom', flat=True)
        M1=list(M)
        N=str(M)
        
        J=[]
        for e in L:
           J=J+str(e.nom)
      
        return M,M1, type(L), type(M)

   afficher_joueurs.short_description = 'Liste des joueurs' 
 """
   


admin.site.register(joueur,joueurAdmin)
admin.site.register(equipe,equipeAdmin)
