from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostingCreateView.as_view()),
    path("/<int:posting_id>", views.PostingView.as_view()),
    path("/comment/<int:posting_id>", views.CommentView.as_view()),
    path("/sub-comment/<int:parent_comment_id>", views.SubCommentView.as_view()),
    path("/list", views.PostingListView.as_view()),
]
