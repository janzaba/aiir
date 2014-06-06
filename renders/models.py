# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Renders(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    start_date = models.DateTimeField('Data stworzenia', auto_now_add=True)
    end_date = models.DateTimeField('Data zakończenia', null=True)
    script = models.TextField(verbose_name='Skrypt sceny')
    status = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Render"
        verbose_name_plural = "Renders"

    def __unicode__(self):
        return self.title