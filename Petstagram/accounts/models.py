from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.accounts.utils import get_gender_choices
from Petstagram.validators.account_validators import alphanumeric_validator


class UserProfile(models.Model):
    GENDER_CHOICES = get_gender_choices()

    username = models.TextField(
        blank=False,
        null=False,
    )

    password = models.TextField(
        blank=False,
        null=False,
    )

    email_address = models.EmailField(
        blank=False,
        null=False
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            alphanumeric_validator,

        ),
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            alphanumeric_validator,
        )
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        blank=True,
        null=True,
        choices=GENDER_CHOICES,
    )
