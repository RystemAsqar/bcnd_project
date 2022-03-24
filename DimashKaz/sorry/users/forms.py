# from django.forms import ModelForm
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from .models import Order

# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args,**kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
        
#     username = forms.CharField(widget = forms.TextInput(attrs = {
#         "class": "input",
#         "type": "text",
#         "placeholder": "enter username"
#     }), label ="Username")

#      password = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "input",
#         "type": "password",
#         "placeholder": "enter password"
#     }))

# class UserRegistrationForm(UserCreationForm):

    
#     class Meta:
#         models = User
#         fields = [ 'username', 'email',]