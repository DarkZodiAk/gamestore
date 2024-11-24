from django.db import models
class Games(models.Model):
    name = models.TextField(blank=True, default='')
    price = models.TextField(blank=True, default='')
    image = models.ImageField(blank=True, default='fallback.png')
    rating = models.TextField(blank=True, default='')
    tags = models.TextField(blank=True, default='')
    genre = models.TextField(blank=True, default='')
    language = models.TextField(blank=True, default='')
    release_date = models.TextField(blank=True, default='')
    publisher = models.TextField(blank=True, default='')
    developer = models.TextField(blank=True, default='')
    features = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    class Meta:
        db_table = 'games'
