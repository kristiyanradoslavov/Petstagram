from django.shortcuts import render

from Petstagram.photos.models import PetPhoto


def add_photo(request):
    return render(
        request,
        "photos/photo-add-page.html"
    )


def photo_details(request, pk):
    current_photo = PetPhoto.objects.get(pk=pk)
    likes = current_photo.like_set.all()
    comments = current_photo.comment_set.all()

    context = {
        'photo': current_photo,
        'likes': likes,
        'comments': comments
    }

    return render(
        request,
        "photos/photo-details-page.html",
        context
    )


def edit_photo(request, pk):
    return render(
        request,
        "photos/photo-edit-page.html",
    )
