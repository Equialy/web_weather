from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название локации', db_index=True)
    userid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, null=False,
                               related_name='users')
    latitude = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='Широта локации')
    longitude = models.DecimalField(max_digits=20, decimal_places=10, verbose_name='Долгота локации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name'])
        ]
