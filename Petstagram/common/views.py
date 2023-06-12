from django.shortcuts import render, redirect

from Petstagram.common.models import Like
from Petstagram.photos.models import PetPhoto


def photo_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo


def apply_user_likes_photo(photo):
    # TODO: fix this the authentications is available
    photo.is_liked = photo.likes_count > 0
    return photo


def home(request):
    all_photos = [photo_likes_count(photo) for photo in PetPhoto.objects.all()]
    all_photos = [apply_user_likes_photo(photo) for photo in all_photos]

    context = {
        "all_photos": all_photos,
    }
    return render(request, "common/home-page.html", context)


def get_user_liked_photos(photo_id):
    photo_likes = Like.objects.filter(to_photo=photo_id)
    return photo_likes


def like_functionality(request, photo_id):
    liked_photos = get_user_liked_photos(photo_id)
    if liked_photos:
        liked_photos.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
