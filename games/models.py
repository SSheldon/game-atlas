from django.db import models, connection, transaction

from game_atlas.utils.models import dict_fetch_all, dict_fetch_one

class Genre(models.Model):

    class Meta:
        managed = False
        db_table = 'genre'

    @staticmethod
    def select_all():
        cursor = connection.cursor()

        query = 'SELECT id, name FROM genre'
        cursor.execute(query)

        return dict_fetch_all(cursor)

class Game(models.Model):

    class Meta:
        managed = False
        db_table = 'game'

    @staticmethod
    def select_all():
        cursor = connection.cursor()

        query = """
            SELECT game.id, game.title, genre.name as "genre_name"
            FROM game JOIN genre ON game.genre_id=genre.id
        """
        cursor.execute(query)

        return dict_fetch_all(cursor)

    @staticmethod
    def select(game_id):
        cursor = connection.cursor()

        query = """
            SELECT game.id, title, genre_id, genre.name as "genre_name"
            FROM game JOIN genre ON game.genre_id=genre.id
            WHERE game.id = %s
        """
        cursor.execute(query, (game_id,))

        return dict_fetch_one(cursor)

    @staticmethod
    def insert(title, genre_id):
        cursor = connection.cursor()

        query = 'INSERT INTO game (title, genre_id) VALUES (%s, %s) RETURNING id'
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

    @staticmethod
    def find(title):
        cursor = connection.cursor()
        search= title + "%"
        query = 'SELECT title FROM game WHERE title LIKE %s'
        cursor.execute(query, (search,))

        return dict_fetch_all(cursor)

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

        query = """
            SELECT game.title, release.release_date,
            genre.name as "genre_name", platform.name as "platform_name"
            FROM release
            JOIN game ON release.game_id=game.id
            JOIN platform ON release.platform_id=platform.id
            JOIN genre ON game.genre_id=genre.id
        """
        cursor.execute(query)

        return dict_fetch_all(cursor)
