from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели News
    '''
    class Meta:
        model = News
        fields = '__all__'
