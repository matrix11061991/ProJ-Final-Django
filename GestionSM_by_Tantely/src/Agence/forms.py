from django import forms



from Agence.models import User
#from bootstrap4.forms import BootstrapMixin



class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=100,required=True)
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField()
    email = forms.EmailField()
    but = forms.CharField(widget=forms.Textarea)
    password= forms.CharField(min_length=6,widget=forms.PasswordInput())

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("le pseudo ne peut pas contenir de $")
        return pseudo
    #motdepasse validation

class FormAjout(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "nom",
            "prenom",
            "adresse",
            "motdepasse",
        ] 
        labels = {"username": "Pseudo",
                  "motdepasse": "Mot de Passe"
                  }
        widgets = {
            "motdepasse": forms.PasswordInput()
        }
        min_length = {
            "motdepasse":5
        }
        