# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from store.models import Book


EMPTY = {'null': True, 'blank': True}
# Create your models here.


class RequestSat(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    uri = models.CharField(max_length=2000)
    status_code = models.IntegerField()
    user_agent = models.CharField(max_length=1000, **EMPTY)
    remote_addr = models.GenericIPAddressField()
    remote_addr_fwd = models.GenericIPAddressField(**EMPTY)
    meta = models.TextField()
    cookies = models.TextField(**EMPTY)
    is_secure = models.BooleanField()
    is_ajax = models.BooleanField()
    user = models.ForeignKey(User, **EMPTY)


class LoggingInfo(models.Model):

    time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_of_book = models.IntegerField()
    id_of_user = models.IntegerField()


def add_info(action, book, user):
    LoggingInfo.objects.create(action=action, book=book, user=user, id_of_book=book.id, id_of_user=user.id)

