from django.urls import path
from workshop_1_first_try.common import views

urlpatterns = [
    path("", views.home_page, name="home-page")
]