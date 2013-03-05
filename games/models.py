from django.db import models

class Genre(models.Model):

    class Meta:
        managed = False
        db_table = 'genre'

class Game(models.Model):

    class Meta:
        managed = False
        db_table = 'game'

class Platform(models.Model):

    class Meta:
        managed = False
        db_table = 'platform'

class Release(models.Model):

    class Meta:
        managed = False
        db_table = 'release'
