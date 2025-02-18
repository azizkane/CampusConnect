# mailjet/views/account_activation.py

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from mailjet.templates.emails import account_activation


# mailjet/views/account_activation.py

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.translation import gettext as _





class PasswordResetView(View):
    def get(self, request, uidb64, token):
        try:
            # Décoder l'uid pour obtenir l'ID de l'utilisateur
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        # Vérifier si le jeton est valide
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, _('Votre compte a été activé avec succès.'))
            return redirect('login')
        else:
            messages.error(request, _('Le lien d\'activation est invalide !'))
            return render(request, 'registration/account_activation_invalid.html')


