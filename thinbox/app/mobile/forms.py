# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class AuthenticationForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
