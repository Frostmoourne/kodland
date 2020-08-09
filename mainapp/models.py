from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128, blank=True)
    img = models.ImageField(upload_to='article_images', blank=True)
    upload = models.DateTimeField(verbose_name='время', auto_now_add=True)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=256, blank=True)
    article = models.TextField(verbose_name='текст', blank=True)
