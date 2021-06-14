from django import forms
from .models import AdvUser

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmaiField(required = True, label = 'Адреса електронної пошти')
    class Mete:
        model = AdvUser
        fields = ('username','email','first_name','last_name','send_messages')
