from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event
def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def reservation(request):
    template = loader.get_template('reservation.html')
    return HttpResponse(template.render())
def formulaire(request):
    template = loader.get_template('salle.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def hebergement(request):
    template = loader.get_template('hebergement.html')
    return HttpResponse(template.render())
def salle_heber(request):
    template = loader.get_template('salle_heber.html')
    return HttpResponse(template.render())
def calendar(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)
