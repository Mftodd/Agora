from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ForumPost(models.Model):
    body = models.TextField(max_length=420)
    review = models.BooleanField(default=False)
    asset = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/post_assets/", blank=True)
    
    def __str__(self):
        return self.body