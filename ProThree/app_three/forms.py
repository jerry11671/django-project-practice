from django import forms
from app_three.models import User

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'