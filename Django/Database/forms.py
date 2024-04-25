from django.forms import ModelForm
from .models import SignIn


class SignInForm(ModelForm):
    class Meta:
        model = SignIn
        fields = ['client', 'course']


