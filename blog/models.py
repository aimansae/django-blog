# MODELS DOCUMENTATION https://docs.djangoproject.com/en/4.1/topics/db/models/

from django.db import models
# https://docs.djangoproject.com/en/4.1/topics/auth/default/

from django.contrib.auth.models import User  # to create users
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, 'Published'))
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)

# to order the fields base on created on date - ascending order

    class Meta:
        ordering = ["-created_on"]

# good practice to put magic method that return a string represent of object
    def __str__(self):
        return self.title
# to reurn total likes of a post

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # to order the fields base on oldest comment first

    class Meta:
        ordering = ["created_on"]

# good practice to put magic method that return a string represent of object
    def __str__(self):
        return self.title
# to reurn the comment

    def __str__(self):
        return f'Comment{self.body} by {self.name}'
    
    # NOW MAKE MIGRATION for every change
    # python3 manage.py makemigrations --dry-run
    # python3 manage.py makemigrations
    # python3 manage.py migrate
