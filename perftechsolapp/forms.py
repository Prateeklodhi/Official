from django import forms
from django.forms import ModelForm, models, widgets
from django.forms.fields import ChoiceField
from .models import Client
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','phone','email','service','project_dec','message']
        widgets = {
        'name': forms.TextInput(attrs={'class':'input','placeholder':'Your Name'}),
        'phone': forms.TextInput(attrs={'class':'input required','placeholder':'Your Phone Number'}),
        'email': forms.EmailInput(attrs={"class":'input required','placeholder':'Your Email Address'}),
        'project_dec':forms.Textarea(attrs={'placeholder':'Project Description','rows':'2' ,'overflow':'scroll'}),
        'message':forms.Textarea(attrs={'placeholder':'Your Message','rows':'2','overflow':'scroll'}),    
        'services': forms.ChoiceField( 
            choices=Client.services,
           
        ),
        

        }