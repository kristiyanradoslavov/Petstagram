from Petstagram.common.models import Like


def photo_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo


def apply_user_likes_photo(photo):
    # TODO: fix this when the authentications is available
    photo.is_liked = photo.likes_count > 0
    return photo


def get_user_liked_photos(photo_id):
    photo_likes = Like.objects.filter(to_photo=photo_id)
    return photo_likes

