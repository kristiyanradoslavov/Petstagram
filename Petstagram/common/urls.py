from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path("like/<int:photo_id>/", views.like_functionality, name='like functionality')
]