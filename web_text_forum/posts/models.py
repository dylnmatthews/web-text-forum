from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    misleading_information = models.BooleanField(default=False)
    predicted_likes = models.IntegerField(default=0)