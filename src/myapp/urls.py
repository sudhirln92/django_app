from django.urls import path
from .views import WebhookView, TestView


urlpatterns = [
    path("test", TestView.as_view(), name="test"),
    path("webhook", WebhookView.as_view(), name="webhook"),
]
