from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="author")
    category = models.CharField(max_length=50)
    body = models.TextField()
    private = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self) :
        return self.title

class Comment(models.Model) :
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="comments")
    post = models.ForeignKey(Post, related_name="comments")
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self) :
        return self.title
