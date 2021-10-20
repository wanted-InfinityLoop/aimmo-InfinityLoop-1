import json

from django.http import JsonResponse
from django.views import View
from django.db.models import Count

from .models import Posting
from core.utils import login_decorator


class PostingListView(View):
    def get(self, request):
        try:
            OFFSET = request.GET.get("offset", 0)
            LIMIT = request.GET.get("limit", 30)

            postings = Posting.objects.all().order_by("-created_time")

            result = {
                "count": postings.aggregate(count=Count("id")).get("count", 0),
                "postings": [
                    {
                        "id": posting.id,
                        "author": posting.author.name,
                        "title": posting.title,
                        "text": posting.text,
                        "created_time": posting.created_time,
                        "updated_time": posting.updated_time,
                    }
                    for posting in postings
                ][OFFSET : LIMIT + OFFSET],
            }

            return JsonResponse({"result": result}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class PostingView(View):
    def get(self, request, posting_id):
        if not Posting.objects.filter(id=posting_id).exists():
            return JsonResponse(
                {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
            )

        posting = Posting.objects.get(id=posting_id)

        result = {
            "id": posting.id,
            "author": posting.author.name,
            "title": posting.title,
            "text": posting.text,
            "created_time": posting.created_time,
            "updated_time": posting.updated_time,
        }
        return JsonResponse({"result": result}, status=200)
