from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from Agence.forms import FormAjout
#from Agence.forms import SignupForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def register(request):

    """if request.method == "POST":
        form  = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci")
    else:
        form =SignupForm()"""
    if request.method == "POST":
         form = FormAjout(request.POST)
         if form.is_valid():
             usersave = form.save(commit=False)
             usersave.save()
         return HttpResponseRedirect(request.path)

    else:
        form = FormAjout()
        
    
        
        
   
    return render(request,'accounts/register.html',{"form":form})
def apropos(request):
    return render(request,'apropos.html')

