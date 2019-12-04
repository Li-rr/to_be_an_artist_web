from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=30)
    passward = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class UserGen(models.Model):
    username = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.username
    def getData(self):
        return self.username,self.title,self.content