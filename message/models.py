from django.db import models

# Create your models here.

# 留言模型

class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text
