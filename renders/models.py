# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Renders(models.Model):
    user = models.ForeignKey(User, verbose_name='Użytkownik')
    created_date = models.DateTimeField('Data dodania', auto_now_add=True)
    finished_date = models.DateTimeField('Data wykonania renderu')
    script = models.TextField('Skrypt sceny')