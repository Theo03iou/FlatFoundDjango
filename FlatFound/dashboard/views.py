from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from property.models import Property

# Create your views here.

@login_required
def index(request):
    properties = Property.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {
        'properties': properties
    })