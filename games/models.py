from django.db import models

class Game(models.Model):

    class Meta:
        managed = False
        db_table = 'game'
