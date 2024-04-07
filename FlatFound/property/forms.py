from django import forms

from .models import Property

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('category', 'property_type', 'price_pcm', 'ppw', 'address', 'postcode', 'num_beds', 'num_bathrooms', 'description', 'image',) 
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
        }),
            'property_type': forms.Select(attrs={
                'class': INPUT_CLASSES
        }),
            'price_pcm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'ppw': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'num_beds': forms.IntegerField(attrs={
                'class': INPUT_CLASSES
        }),
            'num_bathrooms': forms.IntegerField(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }
        
class EditListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('category', 'property_type', 'price_pcm', 'ppw', 'address', 'postcode', 'num_beds', 'num_bathrooms', 'description', 'image',) 
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
        }),
            'price_pcm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'ppw': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'num_beds': forms.IntegerField(attrs={
                'class': INPUT_CLASSES
        }),
            'num_bathrooms': forms.IntegerField(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }