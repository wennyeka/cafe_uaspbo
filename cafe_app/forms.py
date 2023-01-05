from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class FormKoordinat(ModelForm):
    class Meta:
        model = Koordinat
        fields = '__all__'

        widgets = {
            'nama_cafe' : forms.TextInput({'class':'form-control', 'placeholder':'cafe', 'required':'required'}),
            'koordinat' : forms.TextInput({'class':'form-control', 'placeholder':'titik koordinat', 'required':'required'}),
        }

class FormCafe(ModelForm):
    class Meta:
        model = Cafe
        fields = '__all__'

        widgets = {
            'nama_cafe' : forms.TextInput({'class':'form-control', 'placeholder':'cafe', 'required':'required'}),
            'alamat' : forms.TextInput({'class':'form-control', 'placeholder':'alamat', 'required':'required'}),
            'no_tlp' : forms.TextInput({'class':'form-control', 'placeholder':'no_tlp', 'required':'required'}),
            'img' : forms.TextInput({'class':'form-control', 'placeholder':'images', 'required':'required'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
