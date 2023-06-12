# Generated by Django 4.2.1 on 2023-06-08 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0004_alter_petphoto_tagged_pets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.petphoto')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=300)),
                ('date_and_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('to_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.petphoto')),
            ],
        ),
    ]
