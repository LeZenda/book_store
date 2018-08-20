# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name='Book title', max_length=256)
    author = models.CharField(verbose_name='Author info', max_length=256)
    ISBN = models.CharField(verbose_name='International Standard Book Number', max_length=13)
    price = models.IntegerField(verbose_name='Book price (in cents)')
    publish_date = models.DateField(verbose_name='Publish Date', default=datetime.date.today)

    def __str__(self):
        return '{0} - {1}'.format(self.author, self.title)

    def formatted_price(self):
        return '{0:.2f} $'.format(self.price/100.0)
