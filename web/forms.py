from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .mixins import BootstrapMixin

class LoginForm(BootstrapMixin, AuthenticationForm):
    pass

class BootstrapForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
            if type(field) == forms.fields.DateField:
                field.widget.input_type = 'date'
                field.widget.format = '%Y-%m-%d'

