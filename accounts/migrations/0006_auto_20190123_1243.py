# Generated by Django 2.1.4 on 2019-01-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190123_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='头像'),
        ),
    ]
