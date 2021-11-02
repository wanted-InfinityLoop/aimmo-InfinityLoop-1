from django.db import models

from core.models import TimeStamp
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = "categories"


class Posting(TimeStamp):
    title = models.CharField(max_length=128, default="")
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    readers = models.ManyToManyField("users.User", related_name="postings")
    hits = models.IntegerField(default=0)

    class Meta:
        db_table = "postings"


class Comment(TimeStamp):
    content = models.CharField(max_length=216)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "comments"