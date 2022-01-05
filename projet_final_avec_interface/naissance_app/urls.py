from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nouveauNe_list', views.nouveauNe_list, name='nouveauNe_list'),
    path('ajout_newborn', views.ajout_newborn, name='ajout_newborn'),
    path('update_newborn/<nouveau_ne_id>', views.update_newborn, name='update-newborn'), 
    path('delete_newborn/<nouveau_ne_id>', views.delete_newborn, name='delete-newborn'),
    path('show_newborn/<nouveau_ne_id>', views.show_newborn, name='show_newborn'),
    path('search_newborn', views.search_newborn, name='search_newborn'),

    path('user_list', views.user_list, name='user_list'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user/<Utilisateur_id>', views.update_user, name='update_user'),
    path('delete_user/<Utilisateur_id>', views.delete_user, name='delete-user'),
]
