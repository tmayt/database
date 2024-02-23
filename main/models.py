from django.db import models


class Data(models.Model):
    key = models.CharField(max_length=50)
    value = models.TextField()
    user = models.CharField(max_length=50)
    def __str__(self):
        return self.key
    