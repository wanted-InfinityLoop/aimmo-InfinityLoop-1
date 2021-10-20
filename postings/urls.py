from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostingListView.as_view()),
    path("/<int:posting_id>", views.PostingView.as_view()),
]
