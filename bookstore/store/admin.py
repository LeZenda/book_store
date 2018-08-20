# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
from statistic.models import add_info

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'ISBN', 'price',)

    def log_addition(self, request, obj, message):
        super(BookAdmin, self).log_addition(request, obj, message)
        add_info("Create", obj, request.user)

    def log_change(self, request, obj, message):
        super(BookAdmin, self).log_addition(request, obj, message)
        add_info("Update", obj, request.user)

    def log_deletion(self, request, obj, message):
        super(BookAdmin, self).log_addition(request, obj, message)
        add_info("Delete", obj, request.user)
    #
    # def save_model(self, request, obj, form, change):
    #     super(BookAdmin, self).save_model(request, obj, form, change)
    #     add_info('Update' if change else "Create", obj, request.user)


admin.site.register(models.Book, BookAdmin)
