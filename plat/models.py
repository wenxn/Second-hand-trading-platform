from django.db import models
from django.contrib.auth.models import User

class Plat(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Goods, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True,on_delete=models.CASCADE,related_name='+')

    def __str__(self):
        return self.message