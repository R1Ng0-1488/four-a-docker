from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=200,
								 verbose_name='Заголовок')
	text = models.TextField(verbose_name='Описание')
	video = models.URLField(blank=True, null=True, verbose_name='Видео')
	image = models.URLField(blank=True, null=True, verbose_name='Изображение')
	source = models.URLField(blank=True, null=True, verbose_name='Источник')
	author = models.CharField(max_length=200, verbose_name='Автор')
	published = models.DateTimeField(auto_now_add=True,
									 verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'
		ordering = ['-published']

	def __str__(self):
		return self.title


class Videos(models.Model):
	title = models.CharField(max_length=200,
							 verbose_name='Название')
	video = models.URLField(verbose_name='Видео')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
	rubric = models.ForeignKey('Rubrics', on_delete=models.PROTECT,
							   verbose_name='Рубрика', related_name="videos")

	class Meta:
		verbose_name = 'Видео'
		verbose_name_plural = 'Видео'

	def __str__(self):
		return self.title


class Rubrics(models.Model):
	name = models.CharField(max_length=200,
							verbose_name='Название')

	class Meta:
		verbose_name = 'Рубрика'
		verbose_name_plural = 'Рубрики'

	def __str__(self):
		return self.name


class Music(models.Model):
	title = models.CharField(max_length=200, verbose_name='Альбом')
	text = models.TextField(verbose_name='Описание')
	music = models.URLField('Музыка')
	image = models.URLField(blank=True, null=True, verbose_name='Изображение')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Музыка'
		verbose_name_plural = 'Музыка'
		ordering = ['-published']

	def __str__(self):
		return self.title


class Images(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название',
							 blank=True)
	image = models.URLField(verbose_name='Изображение')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Фото'
		verbose_name_plural = 'Фото'
		ordering = ['-published']

	def __str__(self):
		return self.title


class Texts(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название')
	text = models.TextField(verbose_name='Текст')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Текст'
		verbose_name_plural = 'Текста'
		ordering = ['-published']

	def __str__(self):
		return self.title

class Comments(models.Model):
	news = models.ForeignKey(News, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Новости', related_name='comments_news')
	texts = models.ForeignKey(Texts, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Текста', related_name='comments_texts')
	images = models.ForeignKey(Images, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Фотки', related_name='comments_images')
	author = models.CharField(max_length=200, verbose_name='Автор')
	content = models.TextField(verbose_name='Содержание')
	published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Коментарии'
		ordering = ['-published']
