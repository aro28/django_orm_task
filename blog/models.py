from django.db import models
from datetime import date, datetime
# Create your models here.
class AbstractUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(unique=True)


    class Meta:
        abstract = True
        ordering = ['name']

class Author(AbstractUser):
    username = models.CharField(max_length=20, verbose_name='Никнейм')
    date_register = models.DateField(verbose_name='Дата регистрации')

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок статьи')
    authors = models.ManyToManyField(Author, related_name='authors',  through='Publication')

    def __str__(self):
        return self.title

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_published = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.author} -{self.article}'
