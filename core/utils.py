import jwt

from django.http import JsonResponse

from my_settings import MY_SECRET_KEY
from users.models import User


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get("Authorization", None)

            if not (access_token and access_token.startwith("Bearer")):
                return JsonResponse({"message": "AUTH_ERROR"}, status=401)

            payload = jwt.decode(access_token, MY_SECRET_KEY, algorithms="HS256")
            request.user = User.objects.get(id=payload["id"])

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        return func(self, request, *args, **kwargs)

    return wrapper
