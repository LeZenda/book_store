# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand

from store.models import (
    Book,
)
from pprint import pprint

class Command(BaseCommand):

    help = """Returns list of books (default 10 items, asc order)."""

    def add_arguments(self, parser):
        parser.add_argument(
            '--order',
            dest='order',
            default=False,
            help='Specifies the order of sorting (asc/desc).',
            choices=["asc", "desc", ])
        parser.add_argument(
            '--amt',
            dest='amount',
            default="10",
            help='Specifies amount of books to show.')

    def handle(self, *args, **options):

        order = options.get('order')
        try:
            amount = int(options.get('amount'))
            amount = amount if amount > 0 else 10
        except ValueError:
            amount = 10

        if order and order == "asc":
            books = Book.objects.all().order_by('publish_date')[:amount]
        elif order and order == "desc":
            books = Book.objects.all().order_by('-publish_date')[:amount]
        else:
            books = Book.objects.all()[:amount]

        pprint([book.__dict__ for book in books])

