from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


WIND_DIRECTION_CHOICES = {
    'nw': 'СЗ',
    'n': 'С',
    'ne': 'СВ',
    'e': 'В',
    'se': 'ЮВ',
    's': 'Ю',
    'sw': 'ЮЗ',
    'w': 'З',
    'c': 'Штиль'
}

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

class WeatherSummary(models.Model):
    '''
    Модель Сводки погоды
    '''
    sight = models.ForeignKey(
        Sight, on_delete=models.CASCADE, verbose_name='Примечательное место'
    )
    timestamp = models.DateTimeField(verbose_name='Дата')
    temperature = models.IntegerField(
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
        verbose_name='Температура (°C)'
    )
    humidity = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)],
        verbose_name='Влажность (%)'
    )
    pressure = models.PositiveIntegerField(
        validators=[MinValueValidator(700), MaxValueValidator(800)],
        verbose_name='Атмосферное давление (мм.рт.ст.)'
    )
    wind_direction = models.CharField(
        max_length=5,
        verbose_name='Направление ветра'
    )
    wind_speed = models.FloatField(
        validators=[MinValueValidator(0)],
        verbose_name='Скорость ветра (м/с)'
    )

    def __str__(self):
        return f'{self.sight.name} - {self.timestamp.strftime("%d-%m-%Y")}'
    
    class Meta:
        verbose_name = "Сводка погоды"
        verbose_name_plural = "Сводка погоды"
    
    def get_wind_direction_display(self):
        return "test"

    def serialize(self):
        return {
            'sight': self.sight.name,
            'timestamp': self.timestamp.strftime('%d-%m-%Y'),
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'wind_direction': self.wind_direction,
            'wind_speed': self.wind_speed,
        }