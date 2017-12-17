from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns=[
    
    url(r'^planning',TemplateView.as_view(template_name='informations/planning.html')),
    url(r'^partenariats',TemplateView.as_view(template_name='informations/partenariats.html')),
    url(r'^resultats',TemplateView.as_view(template_name='informations/resultats.html')),
    url(r'^teaser',TemplateView.as_view(template_name='informations/teaser.html')),
    
    url(r'^commentSYRendre',TemplateView.as_view(template_name='informations/commentSYRendre.html')),
    url(r'^reglement',TemplateView.as_view(template_name='informations/reglement.html')),
    url(r'^contacts',TemplateView.as_view(template_name='informations/contacts.html')),
    url(r'^tarifs',TemplateView.as_view(template_name='informations/tarifs.html')),
    
    url(r'^soiree',TemplateView.as_view(template_name='informations/soiree.html')),
    url(r'^activites',TemplateView.as_view(template_name='informations/activites.html')),

    url(r'^galeriePhotos',TemplateView.as_view(template_name='informations/galeriePhotos.html')),
    url(r'^palmares',TemplateView.as_view(template_name='informations/palmares.html')),
    
    url(r'^participer', TemplateView.as_view(template_name='informations/participer.html')),
    
    url(r'',TemplateView.as_view(template_name='informations/pageAccueil.html')),
    
    ]
        
