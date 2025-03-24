from django.contrib.auth import get_user_model

from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    User = get_user_model().objects.create_user(
        username=username, password=password
    )

    if email:
        User.email = email
    if first_name:
        User.first_name = first_name
    if last_name:
        User.last_name = last_name

    User.save()
    return User


def get_user(user_id: int) -> User:
    User = get_user_model().objects.get(pk=user_id)
    return User


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    User = get_user(user_id)

    if username:
        User.username = username
    if password:
        User.set_password(password)
    if email:
        User.email = email
    if first_name:
        User.first_name = first_name
    if last_name:
        User.last_name = last_name

    User.save()
    return User
