from django.contrib.auth.forms import AuthenticationForm
from .mixins import BootstrapMixin

class LoginForm(BootstrapMixin, AuthenticationForm):
    pass
