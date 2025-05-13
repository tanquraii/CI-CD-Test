from django.db import models

class CatUser(models.Model):
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname

# Create your models here.
