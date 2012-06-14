# -*- coding: utf-8 -*-

from django.utils.translation import ugettext, ugettext_lazy as _
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, render_to_response, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.conf import settings
from django.views.generic import *

from thinbox.app.mobile import forms as mforms
from thinbox.app.core import models as cmodels

class LoginView(View):
    state = _(u"Please log in below...")
    form = mforms.AuthenticationForm

    def get(self,request,*args,**kwargs):
        if not request.user.is_anonymous():
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request,'mobile/registration/login.html',{ 'form': self.form, 'state': self.state})

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    #create a session tolken for mobile devices can get access
                    request.session[settings.MOBILE_AUTH_TOKEN_NAME] = settings.MOBILE_AUTH_TOKEN_VALUE
                    
                    return redirect(settings.LOGIN_REDIRECT_URL)
                else:
                    self.state = _(u"Your account is not active, please contact the site admin.")
            else:
                    self.state = _(u"Your username and/or password were incorrect.")

        else:
            self.state = _(u"Ops, error below")

        return render(request,'mobile/registration/login.html',{ 'form': form, 'state': self.state})


class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        
        del request.session[settings.MOBILE_AUTH_TOKEN_NAME]
        
        return redirect(settings.LOGIN_URL)


class HomeView(ListView):
    template_name = 'mobile/auth/home.html'
    model = cmodels.Gateway

    def get_context_data(self, **kwargs):
            context = super(HomeView, self).get_context_data(**kwargs)
            context['object_list'] = self.model.objects.filter(usergateways__user=self.request.user).order_by('name')
            return context


class SettingsView(TemplateView):
    template_name = 'mobile/auth/settings.html'

    
