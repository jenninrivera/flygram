from django.db import models
from .authapp.models import Profile
from PIL import Image




class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Profile, related_name='liked_posts')
    comments = models.ManyToManyField('Comment', related_name='post', null=True)


    def __str__(self):
        return self.caption
    
class CrashPadPost(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    location = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class FollowerRelation(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    timestamp = models.DateTimeField(auto_now_add=True)

class SavedPost(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Block(models.Model):
    blocked_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocking')
    blocked_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='blocked')
