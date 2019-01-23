from django.db import models
from accounts.models import UserInfo

class Plat(models.Model):
    plat_name = models.CharField(max_length=30, unique=True)
    plat_description = models.CharField(max_length=100)

    def __str__(self):
        return self.plat_name

class Good(models.Model):
    good_name = models.CharField(verbose_name="闲置名称",max_length=255)
    good_description = models.CharField(verbose_name="闲置描述",max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True)
    plat = models.ForeignKey(Plat, verbose_name="闲置类型",on_delete=models.CASCADE)
    starter = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    price = models.CharField(max_length=100,verbose_name="闲置价格")
    online = models.BooleanField(verbose_name="包邮", default=False)
    lower = models.BooleanField(verbose_name="支持议价", default=False)
    loved = models.BooleanField(verbose_name="收藏", default=False)

    def __str__(self):
        return self.good_name

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Good, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(UserInfo, null=True,on_delete=models.CASCADE,related_name='+')

    def __str__(self):
        return self.message