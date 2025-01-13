from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Index(models.Model):
  title = models.CharField(
    max_length=255,
    verbose_name="Заголовок"
  )
  description = models.TextField(
    verbose_name="Описание"
  )
  logo = models.ImageField(
    upload_to='logo/',
    verbose_name='Логотип'
  )

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = 'Настройка главной страницы'
    verbose_name_plural = "Настройка главной страницы"

class Steps(models.Model):
  img = models.ImageField(
    upload_to='steps/',
    verbose_name='Фото'
  )
  num = models.CharField(
    max_length=255,
    verbose_name='Нумерация'
  )
  title = models.CharField(
    max_length=255,
    verbose_name='Заголовок'
  )
  description = models.TimeField(
    verbose_name='Описание'
  )

  def __str__(self):
    return f"{self.img}"
  
  class Meta:
    verbose_name = "Шаг"
    verbose_name_plural = "Шаги"


class Contact(models.Model):
  title = models.CharField(
      max_length=255,
      verbose_name='Заголовок'
    )
  description = models.TimeField(
      verbose_name='Описание'
    )
  phone = models.CharField(
    max_length=255,
    verbose_name="Номер телефона"
  )
  email  = models.EmailField(
    verbose_name="Email"
  )
  fb = models.URLField(
    verbose_name="facebook"
  )
  ig = models.URLField(
    verbose_name="instagram"
  )
  tt = models.URLField(
    verbose_name="tiktok"
  )

  def __str__(self):
      return self.title
    
  class Meta:
      verbose_name = "Контакты"
      verbose_name_plural = "Контакты"


class Form(models.Model):
   name = models.CharField(_("Название"), max_length=200)


   

class Faq(models.Model):
  title = models.CharField(
      max_length=255,
      verbose_name='Заголовок'
    )
  description = models.TimeField(
      verbose_name='Описание'
    )
  email  = models.EmailField(
    verbose_name="Email"
  )
  
  def __str__(self):
      return self.title
  
  class Meta:
      verbose_name = "Часто задаваемые вопросы"
      verbose_name_plural = "Часто задаваемые вопросы"