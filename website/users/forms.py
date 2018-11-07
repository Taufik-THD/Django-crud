from django.forms import ModelForm
from .models import users

class usersForm(ModelForm):
    
    class Meta:
        model=users
        fields=['username', 'first_name', 'last_name', 'email', 'password']
