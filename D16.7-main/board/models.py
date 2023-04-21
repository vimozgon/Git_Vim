from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from board.resources import CATEGORIES


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORIES, verbose_name='Категория')
    time_public = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    # text = RichTextUploadingField()
    text = RichTextField()


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    time_public = models.DateTimeField(auto_now_add=True)
