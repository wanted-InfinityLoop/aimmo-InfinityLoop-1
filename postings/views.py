import json

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.http import JsonResponse
from django.db.models import Q

from .models import Posting, Category, Comment
from core.utils import login_decorator
from .serializer import PostingSerializer, CommentSerializer


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
            category, _ = Category.objects.get_or_create(name=data["category"])

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

            is_category = data.get("category", None)

            if not is_category:
                return JsonResponse({"message": "Category Needed"}, status=400)
            
            category, _ = Category.objects.get_or_create(name=data["category"])

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

        except Category.DoesNotExist:
            return JsonResponse({"message": "Category not found"}, status=404)

class PostingListView(APIView):
    '''
    # 게시글 목록 불러오기
    '''

    def get(self, request):
        try:
            OFFSET = int(request.GET.get("offset", 0))
            LIMIT = int(request.GET.get("limit", 10))
            CATEGORY = request.GET.get("category", None)
            TITLE = request.GET.get("title", None)
            USER_NAME = request.GET.get("username", None)

            q = Q()

            if CATEGORY:
                q &= Q(category__name = CATEGORY)
            
            if TITLE:
                q &= Q(title__icontains = TITLE)

            if USER_NAME:
                q &= Q(author__name__icontains = USER_NAME)

            postings = Posting.objects.filter(q).order_by("-created_time")[
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

class CommentView(APIView):
    '''
    # 댓글 작성 API
    '''

    # parameter_token = openapi.Parameter(
    #     "Authorization",
    #     openapi.IN_HEADER,
    #     description = "access_token",
    #     type = openapi.TYPE_STRING
    # )
    #@swagger_auto_schema(request_body = CommentSerializer, manual_parameters = [parameter_token])
    @login_decorator
    def post(self, request, posting_id):
        try:
            data = json.loads(request.body)
            user = request.user
            content = data.get('content', None)

            postings = Posting.objects.filter(id = posting_id)

            if not postings.exists():
                return JsonResponse(
                    {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
                )

            posting = Posting.objects.get(id = posting_id)

            comment = Comment.objects.create(
                content = content,
                user = user,
                posting = posting
            )
            
            return JsonResponse({"result": comment.id}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

    
    def get(self, request, posting_id):
        try:
            if not Posting.objects.filter(id = posting_id).exists():
                return JsonResponse(
                    {"message": f"POSTING_{posting_id}_NOT_FOUND"}, status=404
                )

            OFFSET = int(request.GET.get("offset", 0))
            LIMIT = int(request.GET.get("limit", 10))

            comments = Comment.objects.filter(posting_id = posting_id)[OFFSET : OFFSET + LIMIT]

            result = {
                "comments": [
                    {
                        "id": comment.id,
                        "username": comment.user.name,
                        "content": comment.content,
                        "parent_comment_id" : comment.parent_comment_id,
                        "created_time": comment.created_time,
                        "updated_at": comment.updated_at,
                    }
                    for comment in comments
                ],
            }

            return JsonResponse({"result": result}, status = 200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)


class SubCommentView(APIView):
    '''
    # 대댓글 작성 API
    '''

    # parameter_token = openapi.Parameter(
    #     "Authorization",
    #     openapi.IN_HEADER,
    #     description = "access_token",
    #     type = openapi.TYPE_STRING
    # )
    #@swagger_auto_schema(request_body = CommentSerializer, manual_parameters = [parameter_token])
    @login_decorator
    def post(self, request, parent_comment_id):
        try:
            data = json.loads(request.body)
            user = request.user
            content = data.get('content', None)

            parent_comment = Comment.objects.filter(id = parent_comment_id)

            if not parent_comment.exists():
                return JsonResponse(
                    {"message": f"COMMENT_{parent_comment_id}_NOT_FOUND"}, status=404
                )

            if Comment.objects.get(id = parent_comment_id).parent_comment_id is not None:
                return JsonResponse(
                    {"message": "Can't Leave Comment at Sub Comment"}, status = 400
                )

            comment = Comment.objects.get(id = parent_comment_id)

            comment = Comment.objects.create(
                content = content,
                user = user,
                posting = comment.posting,
                parent_comment_id = parent_comment_id
            )
            
            return JsonResponse({"result": comment.id}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except Comment.DoesNotExist:
            return JsonResponse({"message": "Comment Does not Exist"}, status = 404)
