# Generated by Django 4.2.1 on 2023-06-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, to='pets.pet', verbose_name='tagged pets'),
        ),
    ]
