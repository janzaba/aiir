# -*- coding: utf-8 -*-

from django.contrib import admin

from POVRay.users.models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

admin.site.register(User, UsersAdmin)
