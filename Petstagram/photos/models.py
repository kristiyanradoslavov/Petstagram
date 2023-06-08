from django.db import models
from django.core.validators import MinLengthValidator

from Petstagram.pets.models import Pet
from .validators import validate_file_size


class PetPhoto(models.Model):
    photo = models.ImageField(validators=(validate_file_size,))
    description = models.TextField(null=True, blank=True, max_length=300, validators=(MinLengthValidator(10),))
    location = models.CharField(null=True, blank=True, max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True, verbose_name="tagged pets")
    date_of_publication = models.DateField(auto_now=True)
