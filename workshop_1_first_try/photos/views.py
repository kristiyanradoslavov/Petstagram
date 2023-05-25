from django.shortcuts import render


def add_photo(request):
    return render(request, "photo-add-page.html")


def show_photo(request, pk):
    return render(request, "photo-details-page.html")


def edit_photo(request, pk):
    return render(request, "photo-edit-page.html")
