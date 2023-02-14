# Generated by Django 4.1.6 on 2023-02-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_img', models.ImageField(upload_to='market/')),
                ('slide_title', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, upload_to='market/'),
        ),
    ]