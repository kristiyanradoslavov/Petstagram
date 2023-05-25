from django.urls import path, include
from workshop_1_first_try.pets import views

urlpatterns = [
    path("add/", views.add_pets, name='add-pets'),
    path("<str:username>/pet/<slug:petname>/", include([
        path("", views.show_pet, name="show-pet"),
        path("edit/", views.edit_pet, name="edit-pet"),
        path("delete/", views.delete_pet, name="delete-pet")
    ]))
]
