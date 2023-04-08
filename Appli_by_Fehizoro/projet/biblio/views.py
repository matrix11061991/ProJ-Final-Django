from datetime import timezone
from django.views.generic import FormView
from django.shortcuts import render

from biblio.forms import BiblioForm
from biblio.models import Livre  
    
import io
from django.http import FileResponse
from PyPDF2 import PdfFileReader

from django.views.generic import ListView,DetailView
from .models import Livre
# Create your views here.

class ListeLivresView(ListView):
    model = Livre
    template_name = 'liste_livres.html'
    context_object_name = "livres"
    
class BiblioFormView(FormView):
    template_name = "biblio.html"
    form_class = BiblioForm

class ArticleDetailView(DetailView):
    model = Livre
    template_name = 'detail_livres.html'
    context_object_name = "livres"
    

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context["now"] = timezone.now()
        #return context
    
    

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')
