from django.urls import path

from async_logstash_memory_leak.views import ok_view

urlpatterns = [
    path('', ok_view),
]
