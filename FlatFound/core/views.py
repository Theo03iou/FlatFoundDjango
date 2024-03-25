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
    