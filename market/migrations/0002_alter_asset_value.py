# Generated by Django 4.1.7 on 2023-02-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='value',
            field=models.CharField(max_length=24),
        ),
    ]
