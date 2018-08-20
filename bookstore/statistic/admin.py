# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.


class RequestStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'path', 'method', 'user',)


class LoggingInfoStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'user', 'id_of_user', 'book', 'id_of_book', 'time',)

    list_filter = ('action',)


admin.site.register(models.RequestSat, RequestStatAdmin)
admin.site.register(models.LoggingInfo, LoggingInfoStatAdmin)
