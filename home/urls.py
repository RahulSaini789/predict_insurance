from django.urls import path
from home import views

urlpatterns = [
    path("", views.homes, name="homes"),
    path("about/", views.about, name="about"),
    path("prediction", views.prediction, name="prediction"),
    path("contact/", views.contact, name="contact")
]