# Generated by Django 3.0.7 on 2020-08-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='заголовок')),
                ('img', models.ImageField(blank=True, upload_to='article_images')),
                ('desc', models.TextField(blank=True, verbose_name='описание статьи')),
            ],
        ),
    ]
