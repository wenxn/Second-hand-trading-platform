# Generated by Django 2.1.4 on 2019-01-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190123_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='姓名'),
        ),
    ]