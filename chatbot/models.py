from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
