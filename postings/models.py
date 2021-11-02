from django.db import models

from core.models import TimeStamp


class Category(models.Model):
    name = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = "categories"


class Posting(TimeStamp):
    title = models.CharField(max_length=128, default="")
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "postings"
