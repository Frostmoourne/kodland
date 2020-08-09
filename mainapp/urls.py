from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('article/<int:pk>/', mainapp.article, name='article'),
    path('add/', mainapp.add, name='add')
]