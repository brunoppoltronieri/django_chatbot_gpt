from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    
class Feedbacks(models.Model):
    user_id = models.IntegerField(null=True)
    chat_id = models.IntegerField(null=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField()
    message_group = models.IntegerField(null=True)
    approved = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    
class API_KEY(models.Model):
    api_key = models.TextField(null=False)