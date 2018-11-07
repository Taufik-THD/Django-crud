from django.forms import ModelForm
from .models import status

class statusForm(ModelForm):
    
    class Meta:
        model=status
        fields=['message', 'user_id']