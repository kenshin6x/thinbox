# -*- coding: utf-8 -*-
from thinbox.app.core import models as cmodels
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin, UserChangeForm as DjangoUserChangeForm

class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('Gateways'), {'fields': ('gateways',)}),
    )
    form = UserChangeForm

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

class GatewayAdmin(admin.ModelAdmin):
    list_display = ['name','access_method','access_login',\
    'access_password','access_ip','access_port']

admin.site.register(cmodels.Gateway,GatewayAdmin)