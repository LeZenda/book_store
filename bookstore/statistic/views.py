# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import View

import models

# Create your views here.


class RequestList(View):
    """
    Api to get list of sources that should be tested for latency by server
    """
    template_name = "request_list.html"

    def get(self, request, *args, **kwargs):
        context = dict()

        context['request_list'] = models.RequestSat.objects.all().order_by('-time')[:10]

        return render(request, self.template_name, context)
