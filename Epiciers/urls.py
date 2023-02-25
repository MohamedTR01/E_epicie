from django import views
from django.urls import path
from Epiciers import views
from django.contrib.auth import views as auth_view





urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.logIn,name='login'),
    path('register',views.register,name='register'),
    path('contacte/',views.contacte,name='contacte'),
    path('client/',views.client,name='client'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('ac/',views.ajouter_client,name='ac'),
    path('mc/<str:pk>',views.modifier_client,name='mc'),
    path('sc/<str:pk>',views.supprimer_client,name='sc'),
    path('produit',views.produit,name='produit'),
    path('ap/',views.ajouter_produit,name='ap'),
    path('mp/<str:pk>',views.modifier_produit,name='mp'),
    path('sp/<str:pk>',views.supprimer_produit,name='sp'),

    path('view',views.myview,name='view'),
    
]
