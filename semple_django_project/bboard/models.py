from django.db import models


class BboardPost(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
