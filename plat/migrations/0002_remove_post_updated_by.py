# Generated by Django 2.1.4 on 2019-01-26 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_by',
        ),
    ]
