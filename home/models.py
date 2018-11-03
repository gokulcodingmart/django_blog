from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=60, null=True)
	description = models.TextField(null=True)
	category = models.CharField(max_length=20, null=True)

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	description = models.TextField()
<<<<<<< HEAD
=======
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
>>>>>>> e8dce541aee21b7aefd0822e6ffb52df91687cb0
	
class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	count = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)