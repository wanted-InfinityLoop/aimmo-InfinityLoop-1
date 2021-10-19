from django.db import models


class User(models.Model):
    title = models.CharField(max_length=32, null=True)
    text = models.CharField(max_length=64, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "postings"
