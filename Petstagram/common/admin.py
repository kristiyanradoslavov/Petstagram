from django.contrib import admin
from .models import Like, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "date_and_time_of_publication"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["id"]
