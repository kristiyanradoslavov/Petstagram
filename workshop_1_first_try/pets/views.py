from django.shortcuts import render


def add_pets(request):
    return render(request, "pet-add-page.html")


def show_pet(request, username, petname):
    return render(request, "pet-details-page.html")


def edit_pet(request, username, petname):
    return render(request, "pet-edit-page.html")


def delete_pet(request, username, petname):
    return render(request, "pet-delete-page.html")
