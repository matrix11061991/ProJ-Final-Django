from django import forms

from biblio.models import Livre

class BiblioForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = [
            'titre',
        ]
    