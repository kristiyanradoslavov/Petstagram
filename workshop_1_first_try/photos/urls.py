from django.urls import path, include
from workshop_1_first_try.photos import views

urlpatterns = [
    path('add/', views.add_photo, name="add-photo"),
    path("<int:pk>/", include([
        path("", views.show_photo, name="show-photo"),
        path("edit/", views.edit_photo, name='edit-photo')
    ]))
]
