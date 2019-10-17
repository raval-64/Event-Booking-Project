from django import forms
from .models import booking
from phonenumber_field.formfields import PhoneNumberField

class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'textbox', 'placeholder': 'Enter Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Enter Email'}))
    mobile = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Mobile No.','maxlength':'14','pattern':'^\+?\d{0,13}'}))
    
    class Meta:
        model = booking
        fields = ['name','email','mobile']