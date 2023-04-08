from django.urls import path
from . import views



urlpatterns = [
    path('findAll/', views.findAll),
    path('findByProject/<int:id>', views.findByProject),
    path('findOneByPk/<int:id>', views.findOneByPk),
    path('add/<int:id>', views.createPersonnel),
    path('addGroupe/<int:id_projets>', views.createGroupe),
    path('update/<int:id>', views.update),
    
]

#path("delete/<int:id>", views.deleteBlog)