# Generated by Django 2.1.4 on 2019-01-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190123_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Institute',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='学院'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='introduce',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='个人介绍'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='latest_login_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='最近登录时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='student_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='学号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]