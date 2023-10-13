from django.db import models
BookNum = 0
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255, default = ' ')
    def __str__(self):
        return self.title