from django.db import models, connection

def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

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

    @staticmethod
    def select_all():
        cursor = connection.cursor()

        cursor.execute(
            'SELECT game.title, release.release_date, '
            'genre.name as "genre_name", platform.name as "platform_name" '
            'FROM release '
            'JOIN game ON release.game_id=game.id '
            'JOIN platform ON release.platform_id=platform.id '
            'JOIN genre ON game.genre_id=genre.id '
        )

        return dict_fetch_all(cursor)
