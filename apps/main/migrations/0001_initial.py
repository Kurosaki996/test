# Generated by Django 5.1.4 on 2024-12-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=155, verbose_name="Заголовок")),
                ("image", models.ImageField(upload_to="settings", verbose_name="Фото")),
                (
                    "description_image",
                    models.TextField(verbose_name="Описание фотографий"),
                ),
                (
                    "title2",
                    models.CharField(max_length=155, verbose_name="Заголовок 2"),
                ),
            ],
            options={
                "verbose_name_plural": "Настройки Главной Страницы",
            },
        ),
    ]