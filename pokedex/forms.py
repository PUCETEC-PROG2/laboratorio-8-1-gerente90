from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        # labels = {
        #     'name': 'Name',  # Cambiar el texto de la etiqueta
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), #'style': 'font-weight: bold; color: red;'}
            'type': forms.Select(attrs={'class':'form-control'}),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'trainer': forms.Select(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control'})
        }
        