# Generated by Django 4.1.7 on 2023-02-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forumpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='asset',
            field=models.IntegerField(null=True),
        ),
    ]
