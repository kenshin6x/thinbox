# -*- coding: utf-8 -*-
from django.db import models
from thinbox.app.core import constants as cconstants
from django.contrib.auth.models import User

class Gateway(models.Model):
    name = models.CharField(max_length=100)
    access_method = models.IntegerField(choices=cconstants.ACCESS_METHOD,default=cconstants.ACCESS_METHOD_SSH)
    access_login = models.CharField(max_length=50)
    access_password = models.CharField(max_length=50)
    access_ip = models.IPAddressField()
    access_port = models.IntegerField(default=22)

    class Meta:
        verbose_name = 'Gateway'
        verbose_name_plural = 'Gateways'

    def __unicode__(self):
        return self.name


User.add_to_class('gateways', models.ManyToManyField(Gateway,blank=True,null=True))

class User(User):
    class Meta:
        proxy = True
        permissions = (
            ("can_list_gateways", "Can list gateways"),
        )

class UserGateways(models.Model):
    user = models.ForeignKey(User)
    gateway = models.ForeignKey(Gateway)

    class Meta:
        db_table = 'auth_user_gateways'
