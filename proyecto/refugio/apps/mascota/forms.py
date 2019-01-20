from django import forms
from apps.mascota.models import Mascota
class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'edad_aproximada',
            'fecha_rescate',
            'sexo',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre' : 'Nombre', 
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha Rescate',
            'sexo': 'Sexo',
            'persona': 'Adoptante',
            'vacuna': 'Vacuna',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class': 'form-control'}),
            'sexo':forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }