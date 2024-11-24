from django.contrib.auth.models import User
from django.db import models
from games.models import Games


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    class Meta:
        db_table = 'basket'
