from django import forms

class DeporteFormulario(forms.Form):
    deporte = forms.CharField()
    dia = forms.CharField()

class BuscaDeporteForm(forms.Form):
    deporte = forms.TextInput()
