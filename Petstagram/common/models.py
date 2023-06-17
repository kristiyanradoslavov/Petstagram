from django.db import models

from Petstagram.photos.models import PetPhoto


class Comment(models.Model):
    comment_text = models.TextField(
        max_length=300
    )

    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True
    )

    to_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_and_time_of_publication', ]


class Like(models.Model):
    to_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE
    )
