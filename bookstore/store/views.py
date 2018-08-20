# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import View, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

import forms
import models

from statistic.models import add_info

# Create your views here.


class BookList(View):
    """
    Api to get list of sources that should be tested for latency by server
    """
    template_name = "book_list.html"

    def get(self, request, *args, **kwargs):
        context = dict()

        context['book_list'] = models.Book.objects.all()

        return render(request, self.template_name, context)


class AddBookView(CreateView):
    template_name = 'book_form.html'
    model = models.Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, *args, **kwargs):
        context = super(AddBookView, self).get_context_data(*args, **kwargs)
        context['form'] = forms.BookForm
        return context

    def form_valid(self, form):
        obj = form.save()
        add_info("Update", obj, self.request.user)
        return super(AddBookView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class UpdateBookView(UpdateView):
    template_name = 'book_form.html'
    model = models.Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')

    def get_object(self, *args, **kwargs):
        book = get_object_or_404(
            models.Book, id=self.kwargs['id']
        )
        return book

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateBookView, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        obj = form.save()
        add_info("Update", obj, self.request.user)
        return super(UpdateBookView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
