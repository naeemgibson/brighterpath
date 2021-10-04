from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Respite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, default="Respite Note")
    staff = models.CharField(max_length=200, default="staff person")
    date = models.DateField(default= '2021-01-01')
    start = models.TimeField()
    end = models.TimeField()
    notes = models.TextField(null=True, blank=True)
    documents = models.FileField(upload_to='media/', null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return self.author