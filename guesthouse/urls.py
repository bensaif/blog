from django.urls import path
from django.contrib import admin
from guesthouse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guesthouse/', views.index, name='index'),
    path('guesthouse/index.html', views.index, name='index'),
    path('guesthouse/reservation/', views.reservation, name='reservation'),
    path('guesthouse/salle/', views.salle_form_view, name='salle_form'),
    path('guesthouse/inscription.html/', views.inscription, name='inscription'),
    path('guesthouse/connexion.html/', views.connexion, name='connexion'),
    path('guesthouse/hebergement/', views.hebergement_form_view, name='hebergement'),
    path('guesthouse/salle_heber/', views.salle_heber_form_view, name='salle_heber'),
    path('guesthouse/calendar/', views.calendar, name='calendar'),
]
