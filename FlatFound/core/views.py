from django.shortcuts import render, redirect
from django.contrib.auth import logout
from property.models import Category, Property

from .forms import SignupForm

# Create your views here.

def index(request):
    properties = Property.objects.all()[0:6]
    categories = Category.objects.all
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'properties': properties
    })

def contact(request):
    return render(request, 'core/contact.html')

def infocontact(request):
    return render(request, 'infocontact.html')

def about(request):
    return render(request, 'about.html')                  # these four are the views functions for new pages 

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

def terms(request):
    return render(request, 'terms.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })
    