from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Category(models.Model):
    category_name = models.CharField(unique=True,max_length=255)


class Author(models.Model):
    author_user = models.OneToOneField(User,on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.author_user.name} {self.rating}'

    def update_rating(self):
        pRat = self.post_set.aggregate(post_rat=Sum('rating'))
        post_rating = 0
        post_rating += pRat.get('post_rat')

        cRat = self.author_user.comment_set.aggregate(comm_rat=Sum('rating'))
        comment_rating = 0
        comment_rating += cRat.get('comm_rat')

        self.rating = post_rating * 3 + comment_rating
        self.save()


class Post(models.Model):

    def __str__(self):
        return f'{self.created} {self.post_author.author_user.username} {self.rating} {self.title} {self.preview()}'

    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)
    post_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    news = 'NW'
    article = 'AT'
    choice_post = [
        (news, 'Новость'),
        (article, 'Статья'),
    ]
    type = models.CharField(max_length = 2,
                            choices = choice_post,
                            default = news
                            )


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:123]+'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


class Comment(models.Model):

    def __str__(self):
        return f'{self.created} {self.user.username} {self.rating} {self.text}'

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()