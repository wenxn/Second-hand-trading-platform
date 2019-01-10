from django.db import models
from django.contrib.auth.models import User

class Plat(models.Model):
    plat_name = models.CharField(max_length=30, unique=True)
    plat_description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Goods(models.Model):
    good_name = models.CharField(max_length=255)
    good_description = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    starter = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    price = models.CharField(max_length=100)
    online = models.BooleanField(verbose_name="是否支持线上交易（包邮）", default=False)

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