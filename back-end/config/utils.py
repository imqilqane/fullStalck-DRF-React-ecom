from rest_framework import exceptions
from rest_framework_simplejwt.backends import TokenBackend
from User.models import User


def get_buyer(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    try:
        valid_data = TokenBackend(
            algorithm='HS256').decode(token, verify=False)
        user_id = valid_data['user_id']
        user = User.objects.get(id=user_id)
        return user
    except exceptions.ValidationError as v:
        print('ValidationError => ', v)
