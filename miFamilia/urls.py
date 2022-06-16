#este archivo lo tuve que crear porque no estaba. MIEDOOO
from django.urls import path
from miFamilia import views

urlpatterns = [
    path('', views.inicio),
]
