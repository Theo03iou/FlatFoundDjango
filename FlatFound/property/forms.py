from django import forms

from .models import Property

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('category', 'price_pcm', 'ppw', 'address', 'postcode', 'pet_friendly', 'num_beds', 'description', 'image',) 
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
            'pet_friendly': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
        }),
            'num_beds': forms.TextInput(attrs={
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
        fields = ('category', 'price_pcm', 'ppw', 'address', 'postcode', 'pet_friendly', 'num_beds', 'description', 'image',) 
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
            'pet_friendly': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
        }),
            'num_beds': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }