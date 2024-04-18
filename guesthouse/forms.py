from django import forms
from .models import SalleForm, HebergementForm, Salle_heberForm
from .models import CustomUser

from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')  # Liste des champs à inclure dans le formulaire
        # Vous pouvez personnaliser d'autres attributs du formulaire ici si nécessaire

class SalleFormForm(forms.ModelForm):
    class Meta:
        model = SalleForm
        fields = '__all__'  # Utilisez '__all__' pour inclure tous les champs du modèle

class HebergementFormForm(forms.ModelForm):
    class Meta:
        model = HebergementForm
        fields = '__all__'

class SalleHeberFormForm(forms.ModelForm):
    class Meta:
        model = Salle_heberForm
        fields = '__all__'



