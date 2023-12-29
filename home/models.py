# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Test(models.Model):

    #__Test_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    target = models.CharField(max_length=255, null=True, blank=True)
    hypothesis = models.CharField(max_length=255, null=True, blank=True)
    primary = models.CharField(max_length=255, null=True, blank=True)
    secondary = models.CharField(max_length=255, null=True, blank=True)

    #__Test_FIELDS__END

    class Meta:
        verbose_name        = _("Test")
        verbose_name_plural = _("Test")


class Learnsection(models.Model):

    #__Learnsection_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    card image = models.CharField(max_length=255, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)

    #__Learnsection_FIELDS__END

    class Meta:
        verbose_name        = _("Learnsection")
        verbose_name_plural = _("Learnsection")


class User(models.Model):

    #__User_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
