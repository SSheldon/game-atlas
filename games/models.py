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

    @staticmethod
    def add_genre(genre):
        cursor = connection.cursor()

        query = 'INSERT INTO genre (name) VALUES (%s) RETURNING id'
        cursor.execute(query, (genre,))
        transaction.commit_unless_managed()

        row = cursor.fetchone()

        if not row:
            return None
        return row[0]

    @staticmethod
    def get_genre_id(genre):
        cursor = connection.cursor()

        query = 'SELECT id FROM genre WHERE name = %s'
        cursor.execute(query, (genre,))

        row = cursor.fetchone()
        if not row:
            return Genre.add_genre(genre)
        else:
            return row[0]

class Game(models.Model):

    class Meta:
        managed = False
        db_table = 'game'

    @staticmethod
    def select_all():
        cursor = connection.cursor()

        query = """
            SELECT game.id, game.title, genre.name as "genre_name"
            FROM game JOIN genre ON game.genre_id=genre.id ORDER BY game.title
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
    def select_many(game_ids):
        cursor = connection.cursor()

        query = """
            SELECT game.id, title, genre_id, genre.name as "genre_name"
            FROM game JOIN genre ON game.genre_id=genre.id
            WHERE game.id = ANY(%s)
        """
        cursor.execute(query, (game_ids,))

        return dict_fetch_all(cursor)

    @staticmethod
    def select_many_by_title(titles):
        cursor = connection.cursor()

        query = """
            SELECT id, title FROM game
            WHERE title = ANY(%s)
        """
        cursor.execute(query, (titles,))

        return dict_fetch_all(cursor)

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

    #Used to check to make sure we aren't adding a game that is already in the db
    @staticmethod
    def add_game(title, genre_id):
        cursor = connection.cursor()

        query = """
                    SELECT game.id, title FROM game
                    INNER JOIN genre ON game.genre_id = genre.id
                    WHERE game.title = %s AND genre.id = %s
                """
        cursor.execute(query, (title, genre_id,))

        row = cursor.fetchone()
        if row is None:
            return Game.insert(title, genre_id)
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
        search= "%" + title + "%"
        query = 'SELECT id, title FROM game WHERE title ILIKE %s'
        cursor.execute(query, (search,))

        return dict_fetch_all(cursor)

    @staticmethod
    def game_detail(game_id):
        cursor = connection.cursor()

        query = """
                SELECT game.title, release.release_date, 
                genre.name AS "genre_name", platform.name as "platform_name"
                FROM release
                JOIN game on release.game_id = game.id
                JOIN platform on release.platform_id = platform.id
                JOIN genre ON game.genre_id = genre.id
                WHERE game.id = %s
            """ 

        cursor.execute(query, (game_id,))

        return dict_fetch_all(cursor)

class Platform(models.Model):

    class Meta:
        managed = False
        db_table = 'platform'

    @staticmethod
    def get_platform_id(platform):
        cursor = connection.cursor()

        query = 'SELECT id FROM platform WHERE name = %s'
        cursor.execute(query, (platform,))

        row = cursor.fetchone()
        if not row:
            return Platform.add_platform(platform)
        else:
            return row[0]

    @staticmethod
    def add_platform(platform):
        cursor = connection.cursor()

        query = 'INSERT INTO platform (name) VALUES (%s) RETURNING id'
        cursor.execute(query, (platform,))
        transaction.commit_unless_managed()

        row = cursor.fetchone()

        if not row:
            return None
        return row[0]

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

    @staticmethod
    def game_info(info_dict):

        genre_id = Genre.get_genre_id(info_dict['genre'])
        platform_id = Platform.get_platform_id(info_dict['platform'])
        game_id = Game.add_game(info_dict['title'], genre_id)
        if game_id is not None:
            Release.insert(game_id, platform_id, info_dict['release'])

    @staticmethod
    def insert(game_id, platform_id, release_date):
        cursor = connection.cursor()

        query = 'INSERT INTO release (game_id, platform_id, release_date) VALUES (%s, %s, %s)'

        cursor.execute(query, (game_id, platform_id, release_date,))
        transaction.commit_unless_managed()

    @staticmethod
    def get_game_releases(game_id):
        cursor = connection.cursor()

        query = """
            SELECT game.title, release.release_date,
            genre.name as "genre_name", platform.name as "platform_name"
            FROM release
            JOIN game ON release.game_id=game.id
            JOIN platform ON release.platform_id=platform.id
            JOIN genre ON game.genre_id=genre.id
            WHERE game_id = %s
        """

        cursor.execute(query, (game_id,))

        return dict_fetch_all(cursor)

