from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .forms import NewListingForm, EditListingForm
from .models import Category, Property

# Create your views here.


def property(request):
    query = request.GET.get('query', '')
    length_id = request.GET.get('length', 0)
    length_type = Category.objects.all()
    properties = Property.objects.all()

    return render(request, 'property/listings.html', {
        'properties': properties,
        'query': query,
        'length_type': length_type,
        'length_id': int(length_id)
    })


def detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    related_properties = Property.objects.filter(category=property.category).exclude(pk=pk)[0:3]
    return render(request, 'property/detail.html', {
        'property': property,
        'related_properties': related_properties  
    })
    
@login_required
def new(request):
    if request.method == 'POST':
        form = NewListingForm(request.POST, request.FILES)
        
        if form.is_valid():
            property = form.save(commit=False)
            property.created_by = request.user
            property.save()
            
            return redirect('property:detail', pk=property.id)
    else:
        form = NewListingForm()
    
    return render(request, 'property/form.html', {
        'form': form,
        'title': 'New Property',
        })

@login_required
def edit(request, pk):
    property = get_object_or_404(Property, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditListingForm(request.POST, request.FILES, instance=property)
        
        if form.is_valid():
            form.save()
            
            return redirect('property:detail', pk=property.id)
    else:
        form = EditListingForm(instance=property)
        
    return render(request, 'property/form.html', {
        'form': form,
        'title': 'Edit property',
    })
    
@login_required
def delete(request, pk):
    property = get_object_or_404(Property, pk=pk, created_by=request.user)
    property.delete()
    
    return redirect('dashboard:index')