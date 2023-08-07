from django.contrib import messages
from django.contrib.auth.views import LogoutView

# override dispatch to view logout-message instead of clearing all
class IntranetLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'Sie wurden erfolgreich ausgeloggt.')
        return super().dispatch(request, *args, **kwargs)
