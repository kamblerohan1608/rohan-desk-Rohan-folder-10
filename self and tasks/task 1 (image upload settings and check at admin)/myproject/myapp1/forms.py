from tkinter import Widget
from django import forms
from .models import myappModel

class myappForm(forms.ModelForm):

    class Meta:
        model = myappModel
        fields = ['image_title','image_description','image_photo']

        labels = {
            'image_title':'Image Title :',
            'image_description':'Image Description :',
            'image_photo':'Image Upload :',
        }

        widgets = {
            'image_title':forms.TextInput(attrs={'class':'form-control my-2'}),
            'image_description':forms.TextInput(attrs={'class':'form-control my-2'}),
            'image_upload':forms.FileInput(attrs={'class':'form-control'}),
        }