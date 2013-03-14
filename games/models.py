from django.db import models, connection, transaction

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

    @staticmethod
    def select(game_id):
        cursor = connection.cursor()

        query = (
            'SELECT game.title, genre.name as "genre_name" '
            'FROM game JOIN genre ON game.genre_id=genre.id '
            'WHERE game.id = %s'
        )
        cursor.execute(query, (game_id,))

        row = cursor.fetchone()
        if not row:
            return {}
        return dict(zip((col[0] for col in cursor.description), row))

    @staticmethod
    def insert(title, genre_id):
        cursor = connection.cursor()

        query = (
            'INSERT INTO game (title, genre_id) VALUES (%s, %s) RETURNING id'
        )
        cursor.execute(query, (title, genre_id))
        transaction.commit_unless_managed()

        row = cursor.fetchone()
        if not row:
            return None
        return row[0]

    @staticmethod
    def update(game_id, title, genre_id):
        cursor = connection.cursor()

        query = 'UPDATE game SET title=%s, genre_id=%s WHERE id = %s'
        cursor.execute(query, (title, genre_id, game_id))
        transaction.commit_unless_managed()

    @staticmethod
    def delete(game_id):
        cursor = connection.cursor()

        query = 'DELETE FROM game WHERE id = %s'
        cursor.execute(query, (game_id,))
        transaction.commit_unless_managed()

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
