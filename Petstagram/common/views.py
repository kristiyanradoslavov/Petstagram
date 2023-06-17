from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy # this is used to copy on the clipboard

from Petstagram.common.models import Like
from Petstagram.common.utils import photo_likes_count, apply_user_likes_photo, get_user_liked_photos
from Petstagram.photos.models import PetPhoto


def home(request):
    all_photos = [photo_likes_count(photo) for photo in PetPhoto.objects.all()]
    all_photos = [apply_user_likes_photo(photo) for photo in all_photos]

    context = {
        "all_photos": all_photos,
    }
    return render(request, "common/home-page.html", context)


def like_functionality(request, photo_id):
    liked_photos = get_user_liked_photos(photo_id)
    if liked_photos:
        liked_photos.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')



