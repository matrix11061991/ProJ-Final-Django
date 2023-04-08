from django.urls import path
from . import views



urlpatterns = [
    path('findAll/', views.findAll),
    #path('findOne/', views.findOne),
    path('findOneByPk/<int:id>', views.findOneByPk),
    path('add/<int:fk>', views.create),
    path('update/<int:id>', views.update),
    
]

#path("delete/<int:id>", views.deleteBlog)