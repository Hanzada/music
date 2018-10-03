from django.db import models
from django.shortcuts import reverse


def generate_filename(instanse, filename):
     filename = instanse.slug + '.mp3'
     return "{0}/{1}".format(instanse, filename)
class Genre(models.Model):
    name=models.CharField('Название жанра',max_length=50)
    slug=models.CharField('Слаг жанра',max_length=50)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('genre_detail',args=[str(self.slug)])

    class Meta:
        verbose_name_plural='Жанры'
        verbose_name='Жанр'


class Author(models.Model):

    lastname=models.CharField('Фамилия автора',max_length=50)
    firstname=models.CharField('Имя автора',max_length=50)
    slug=models.SlugField('Слаг автора',max_length=50)
    date_birtday=models.DateTimeField('Дата рождение')
    photo=models.FileField('Фото автора',upload_to='photo',blank=True)
    def __str__(self):
        return '{0} {1}'.format(self.firstname,self.lastname)
    def get_absolute_url(self):
        return reverse('author_detail',args=[str(self.slug)])
    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'


class Audio(models.Model):
    name=models.CharField('Название музыки',max_length=50)
    slug=models.SlugField('Слаг музыки',max_length=50)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    text=models.TextField('Текст музыки',blank=True)
    audio=models.FileField('Музыка',upload_to='audio')
    data_publish=models.DateTimeField('Дата добавлений',auto_now_add=True)
    download=models.PositiveIntegerField('Число загрузок',default=0)
    def get_absolute_url(self):
        return reverse('audio_detail',args=[str(self.slug)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Музыки'
        verbose_name = 'Музыка'


class Video(models.Model):
    name=models.CharField('Название видео',max_length=50)
    slug=models.SlugField('Слаг видео',max_length=50)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    text=models.TextField('Текст видео',blank=True)
    video=models.FileField('Видео',upload_to='video')
    data_publish=models.DateTimeField('Дата добавление',auto_now_add=True)
    download=models.PositiveIntegerField('Число загрузок',default=0)
    def get_absolute_url(self):
        return reverse('video_detail',args=[str(self.slug)])
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Видое'
        verbose_name = 'Видео'


class Image(models.Model):
    name=models.CharField('Название изображений',max_length=50)
    image=models.FileField('Изображение',upload_to='image')
    data_publish=models.DateTimeField('Дата добавление',auto_now_add=True)
    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name_plural = 'Фото'
        verbose_name = 'Фото'






