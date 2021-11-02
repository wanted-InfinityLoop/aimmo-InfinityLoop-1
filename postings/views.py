import json

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.http import JsonResponse

from .models import Posting, Category
from core.utils import login_decorator
from .serializer import PostingSerializer


class PostingView(APIView):
    '''
    # 게시글 불러오기
    '''
    parameter_token = openapi.Parameter(
        "Authorization",
        openapi.IN_HEADER,
        description = "access_token",
        type = openapi.TYPE_STRING
    )

    @swagger_auto_schema(request_body = PostingSerializer, manual_parameters = [parameter_token])
    @login_decorator
    def get(self, request, posting_id):
        if not Posting.objects.filter(id=posting_id).exists():
            return JsonResponse(
                {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
            )
        user = request.user
        posting = Posting.objects.get(id=posting_id)

        if user not in posting.readers.all():
            posting.readers.add(user)
            posting.hits += 1
            posting.save()

        result = {
            "id": posting.id,
            "author": posting.author.name,
            "title": posting.title,
            "text": posting.text,
            "category": posting.category.name,
            "hits": posting.hits,
            "created_time": posting.created_time,
            "updated_at": posting.updated_at,
        }
        return JsonResponse({"result": result}, status=200)    
    
    '''
    # 게시글 수정
    '''
    
    @swagger_auto_schema(request_body = PostingSerializer, manual_parameters = [parameter_token])
    @login_decorator
    def put(self, request, posting_id):
        try:
            if not Posting.objects.filter(id=posting_id).exists():
                return JsonResponse(
                    {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
                )

            data = json.loads(request.body)
            posting = Posting.objects.get(id=posting_id)
            category = Category.objects.get(name=data["category"])

            if request.user.id != posting.author_id:
                return JsonResponse({"message": "FORBIDDEN"}, status=403)

            posting.text = data["text"] 

            if data["category"] != posting.category.name:
                posting.category_id = category.id

            posting.save()

            return JsonResponse(
                {"message": f"{posting.title} has successfully updated"}, status=200
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Category.DoesNotExist:
            return JsonResponse({"message": "Category Does not Exist"}, status=404)


    '''
    # 게시글 삭제
    '''

    @swagger_auto_schema(manual_parameters = [parameter_token])
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


class PostingCreateView(APIView):
    '''
    # 게시글 작성
    '''

    parameter_token = openapi.Parameter(
        "Authorization",
        openapi.IN_HEADER,
        description = "access_token",
        type = openapi.TYPE_STRING
    )
    @swagger_auto_schema(request_body = PostingSerializer, manual_parameters = [parameter_token])
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user

            category = Category.objects.get(name=data["category"])

            posting = Posting.objects.create(
                title=data["title"],
                text=data["text"],
                author=user,
                category=category,
            )

            return JsonResponse(
                {"message": f"{posting.title} has successfully posted"}, status=201
            )
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class PostingListView(APIView):
    '''
    # 게시글 목록 불러오기
    '''

    def get(self, request):
        try:
            OFFSET = int(request.GET.get("offset", 0))
            LIMIT = int(request.GET.get("limit", 10))

            postings = Posting.objects.all().order_by("-created_time")[
                OFFSET : OFFSET + LIMIT
            ]

            result = {
                "count": len(postings),
                "postings": [
                    {
                        "id": posting.id,
                        "author": posting.author.name,
                        "title": posting.title,
                        "text": posting.text,
                        "category": posting.category.name,
                        "created_time": posting.created_time,
                        "updated_at": posting.updated_at,
                    }
                    for posting in postings
                ],
            }

            return JsonResponse({"result": result}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
