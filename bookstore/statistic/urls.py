from django.conf.urls import url
from .views import RequestList

urlpatterns = [
    url(r'^$', RequestList.as_view(), name='request_list'),
]
