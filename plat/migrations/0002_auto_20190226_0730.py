# Generated by Django 2.1.4 on 2019-02-26 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postreply',
            options={'ordering': ['created_at']},
        ),
    ]
