from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event
from .forms import SalleFormForm, HebergementFormForm, SalleHeberFormForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser

from .forms import CustomUserCreationForm

def connexion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            # Gérer l'échec de la connexion
            return render(request, 'connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'connexion.html')


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def reservation(request):
    template = loader.get_template('reservation.html')
    return HttpResponse(template.render())

def salle_form_view(request):
    if request.method == 'POST':
        # Créer une instance du formulaire avec les données de la requête POST
        form = SalleFormForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger vers une page de succès ou effectuer une autre action
    else:
        # Créer une instance vide du formulaire
        form = SalleFormForm()
    
    return render(request, 'salle.html', {'form': form})



def hebergement_form_view(request):
    if request.method == 'POST':
        # Créer une instance du formulaire avec les données de la requête POST
        form = HebergementFormForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger vers une page de succès ou effectuer une autre action
    else:
        # Créer une instance vide du formulaire
        form = HebergementFormForm()
    
    return render(request, 'hebergement.html', {'form': form})

def salle_heber_form_view(request):
    if request.method == 'POST':
        # Créer une instance du formulaire avec les données de la requête POST
        form = SalleHeberFormForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger vers une page de succès ou effectuer une autre action
    else:
        # Créer une instance vide du formulaire
        form = SalleHeberFormForm()
    
    return render(request, 'salle_heber.html', {'form': form})

def calendar(request):
    # Récupérer tous les événements depuis la base de données
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)
