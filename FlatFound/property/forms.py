from django import forms

from .models import Property

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('category', 'price_pcm', 'ppw', 'address', 'postcode', 'description', 'pet_friendly', 'image',) 
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
            'address': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'pet_friendly': forms.BooleanField(),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }
        
class EditListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('category', 'price_pcm', 'ppw', 'address', 'postcode', 'description', 'pet_friendly', 'image',) 
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
            'address': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'pet_friendly': forms.BooleanField(),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }