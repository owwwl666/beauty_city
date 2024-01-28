from django.shortcuts import render
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("registration/", render, kwargs={"template_name": "registration.html"}, name='registration'),
    path("reg/", views.register_user),
    path("reg_succ/", render, kwargs={"template_name": "reg_succ.html"}, name='reg_succ'),
    path("reg_err/", render, kwargs={"template_name": "reg_err.html"}, name='reg_err'),
]
