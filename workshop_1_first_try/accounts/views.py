from django.shortcuts import render


def register(request):
    return render(request, "register-page.html")


def login(request):
    return render(request, "login-page.html")


def show_profile_details(request, pk):
    return render(request, "profile-details-page.html")


def edit_profile(request, pk):
    return render(request, "profile-edit-page.html")


def delete_profile(request, pk):
    return render(request, "profile-delete-page.html")
