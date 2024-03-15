from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('length', 'pcm', 'ppw', 'description', 'address', 'postcode', 'image',) 
        widgets = {
            'length': forms.Select(attrs={
                'class': INPUT_CLASSES
        }),
            'pcm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'ppw': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'address': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }
        
class EditListingForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('length', 'pcm', 'ppw', 'description', 'address', 'postcode', 'image',) 
        widgets = {
            'length': forms.Select(attrs={
                'class': INPUT_CLASSES
        }),
            'pcm': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'ppw': forms.TextInput(attrs={
                'class': INPUT_CLASSES
        }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'address': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'postcode': forms.Textarea(attrs={
                'class': INPUT_CLASSES
        }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
        }),
        }