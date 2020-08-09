from django.forms import ModelForm
from django import forms
from .models import Articles


class NewArticle(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'article', 'img', ]
        labels = {'title': '', 'article': '', 'img': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Введите название статьи'})
        self.fields['img'].widget.attrs.update({'placeholder': 'ЗАГРУЗИТЕ ИЗОБРАЖЕНИЕ', "onchange": "loadImg(event)"})


