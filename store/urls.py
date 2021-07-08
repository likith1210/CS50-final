from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name="store"
urlpatterns=[
    path("", views.my_login, name="login"),
    path("billing", views.billing, name="billing"),
    path("bills", views.bills, name="bills"),
    path("add", views.add, name="add"),
    path("view", views.view, name="view"),
    path("med", views.med, name="medicine")
]