from django.contrib import admin
from Petstagram.pets import models
from Petstagram.photos.models import PetPhoto


@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', "slug", "date_of_birth"]


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "get_tagged_pets"]


    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])
