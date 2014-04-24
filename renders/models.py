# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Renders(models.Model):
    user = models.ForeignKey(User)
    start_date = models.DateTimeField('Data stworzenia', auto_now_add=True)
    end_date = models.DateTimeField('Data zakończenia')
    script = models.TextField(verbose_name='Skrypt sceny')

    class Meta:
        verbose_name = "Render"
        verbose_name_plural = "Renders"

    def __unicode__(self):
        return self.title