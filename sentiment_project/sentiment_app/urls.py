from django.urls import path
from sentiment_app import views

urlpatterns = [
    path("", views.index, name="index"),
]
