import json

from django.http import JsonResponse
from django.views import View

from .models import Posting
from core.utils import login_decorator


class PostingListView(View):
    def get(self, request):
        try:
            OFFSET = request.GET.get("offset", 0)
            LIMIT = request.GET.get("limit", 30)

            postings = Posting.objects.all().order_by("-created_time")[
                OFFSET : LIMIT + OFFSET
            ]

            return
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
