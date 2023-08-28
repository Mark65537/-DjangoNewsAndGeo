import requests
from celery import shared_task
from DjangoNewsAndGeo.settings import WEATHER_API_KEY
from .models import WIND_DIRECTION_CHOICES, WeatherSummary, Sight


@shared_task
def fetch_weather_data():
    '''
    Функция получения сводки погоды
    '''
    sights = Sight.objects.all()
    for sight in sights:
        url = f'https://api.weather.yandex.ru/v2/forecast?lat={sight.latitude}&lon={sight.longitude}&lang=ru_RU'
        yaheader = {
            'X-Yandex-API-Key': WEATHER_API_KEY
        }
        response = requests.get(url, headers=yaheader)
        if response.status_code == 200:
            weather_data = response.json()
            temperature = weather_data['fact']['temp']
            humidity = weather_data['fact']['humidity']
            pressure = weather_data['fact']['pressure_mm']
            wind_direction = WIND_DIRECTION_CHOICES[weather_data['fact']['wind_dir']]
            wind_speed = weather_data['fact']['wind_speed']
            timestamp = weather_data['now_dt']
            WeatherSummary.objects.create(
                sight=sight,
                timestamp=timestamp,
                temperature=temperature,
                humidity=humidity,
                pressure=pressure,
                wind_direction=wind_direction,
                wind_speed=wind_speed
            )
