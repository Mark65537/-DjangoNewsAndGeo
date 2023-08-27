from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


class Sight(models.Model):
    '''
    Модель для Примечательного места
    '''
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    class Meta:
        verbose_name = "Примечательное место"
        verbose_name_plural = "Примечательные места"

    def save(self, *args, **kwargs):
        self.latitude = round(self.latitude, 8)
        self.longitude = round(self.longitude, 8)
        self.latitude = float(f'{self.latitude:.8f}')
        self.longitude = float(f'{self.longitude:.8f}')
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
