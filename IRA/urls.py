"""IRA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guesthouse.views import index,reservation,formulaire,login,hebergement,salle_heber,calendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guesthouse/', index,name='index'),
     path('guesthouse/index.html', index,name='index'),
    path('guesthouse/reservation.html/', reservation,name='reservation'),
     path('guesthouse/reservation.html/formulaire.html', formulaire,name='formulaire'),
      path('guesthouse/login.html', login,name='login'),
    path('guesthouse/reservation.html/hebergement.html', hebergement,name='hebergement'),
    path('guesthouse/reservation.html/salle_heber.html', salle_heber,name='salle_heber'),
     path('guesthouse/reservation.html/calendar.html', calendar,name='calendar'),
]
