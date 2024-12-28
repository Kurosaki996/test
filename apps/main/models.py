from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=155,verbose_name='Заголовок')
    image = models.ImageField(upload_to='settings', verbose_name='Фото')
    description_image = models.TextField(verbose_name='Описание фотографий')
    title2 = models.CharField(max_length=155,verbose_name='Заголовок 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Главной Страницы'

class Settings_All(models.Model):
    title = models.CharField(max_length=155,verbose_name='Заголовок')
    static = models.IntegerField(verbose_name='Статистика')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Статистика в Главном Странице'
