from django.urls import path, include
from Petstagram.common.views import home, like_functionality, share_functionality

urlpatterns = [
    path('', home, name="home_page"),
    path("like/<int:photo_id>/", like_functionality, name='like functionality'),
    path('share/<int:photo_id>/', share_functionality, name='share functionality')
]