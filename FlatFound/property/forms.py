from django import forms

from .models import Property

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('country', 'city', 'category',  'price_pcm', 'ppw', 'address', 'postcode',
                  'pet_friendly', 'number_of_beds', 'number_of_bathrooms', 'description', 'image1', 'image2', 'image3', 'image4',)
        widgets = {
            'country': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
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
            'number_of_beds': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'number_of_bathrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image1': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image2': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image3': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image4': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditListingForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('country', 'city', 'category',  'price_pcm', 'ppw', 'address', 'postcode',
                  'pet_friendly', 'number_of_beds', 'number_of_bathrooms', 'description', 'image1', 'image2', 'image3', 'image4',)
        widgets = {
            'country': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
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
            'number_of_beds': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'number_of_bathrooms': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image1': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image2': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image3': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image4': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
