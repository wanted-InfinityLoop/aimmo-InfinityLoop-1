import jwt

from django.http import JsonResponse

# from my_setting import MY_SECRET_KEY
from config.settings import SECRET_KEY
from users.models import User


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            auth_header = request.headers.get("Authorization", None)
            print(auth_header, '흠')
            # if not (auth_header and auth_header.startswith("Bearer ")):
            #     return JsonResponse({"message": "AUTH_ERROR"}, status=401)

            # token = auth_header.split(" ")[1]

            payload = jwt.decode(auth_header, SECRET_KEY, algorithms="HS256")
            request.user = User.objects.get(id=payload["id"])

        except jwt.exceptions.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)

        return func(self, request, *args, **kwargs)

    return wrapper
