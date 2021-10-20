import json

from django.http import JsonResponse
from django.views import View
from django.db.models import Count

from .models import Posting
from core.utils import login_decorator


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
            "updated_at": posting.updated_at,
        }
        return JsonResponse({"result": result}, status=200)

    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            posting = Posting.objects.create(
                title=data["title"],
                text=data["text"],
                author=user,
            )

            return JsonResponse(
                {"message": f"{posting.title} has successfully posted"}, status=201
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    @login_decorator
    def put(self, request, posting_id):
        try:
            if not Posting.objects.filter(id=posting_id).exists():
                return JsonResponse(
                    {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
                )

            posting = Posting.objects.get(id=posting_id)

            if request.user.id != posting.author_id:
                return JsonResponse({"message": "FORBIDDEN"}, status=403)

            data = json.loads(request.body)
            posting.text = data["text"]
            posting.save()

            return JsonResponse(
                {"message": f"{posting.title} has successfully updated"}, status=200
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    @login_decorator
    def delete(self, request, posting_id):
        try:
            if not Posting.objects.filter(id=posting_id).exists():
                return JsonResponse(
                    {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
                )

            posting = Posting.objects.get(id=posting_id)

            if request.user.id != posting.author_id:
                return JsonResponse({"message": "FORBIDDEN"}, status=403)

            posting.delete()

            return JsonResponse(
                {"message": f"{posting.title} has successfully deleted"}, status=204
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class PostingListView(View):
    def get(self, request):
        try:
            OFFSET = int(request.GET.get("offset", 0))
            LIMIT = int(request.GET.get("limit", 10))

            postings = Posting.objects.all().order_by("-created_time")[
                OFFSET : OFFSET + LIMIT
            ]

            result = {
                "count": postings.aggregate(count=Count("id")).get("count", 0),
                "postings": [
                    {
                        "id": posting.id,
                        "author": posting.author.name,
                        "title": posting.title,
                        "text": posting.text,
                        "created_time": posting.created_time,
                        "updated_at": posting.updated_at,
                    }
                    for posting in postings
                ],
            }

            return JsonResponse({"result": result}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
