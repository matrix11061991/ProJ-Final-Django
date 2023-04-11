from django.urls import path

from projet.views import base
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('liste/', ListeLivresView.as_view(), name='liste_livres'),
    path('biblio/<str:slug>/', ArticleDetailView.as_view(), name='detail_livres'),
    #path('',base , name='base')
    # autres URLs de votre application
]