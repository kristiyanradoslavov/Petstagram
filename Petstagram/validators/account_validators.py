from django.core.exceptions import ValidationError


def alphanumeric_validator(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters!')
