"""
Definition of models.
"""

from django.db import models
from django.urls import reverse

class News(models.Model):
    """Модель новости"""
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.pk)])
