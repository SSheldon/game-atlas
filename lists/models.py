from django.db.models import Model

from game_atlas.utils.models import dict_fetch_all

class UserGame(Model):

    class Meta:
        managed = False
        db_table = 'user_game'

    @staticmethod
    def get_games(user_id):
        cursor = connection.cursor()

        query = """
            SELECT game.title, genre.name as "genre_name"
            FROM user_game
            JOIN game on user_game.game_id=game.id
            JOIN genre ON game.genre_id=genre.id
            WHERE user_game.user_id = %s
        """
        cursor.execute(query, (user_id,))

        return dict_fetch_all(cursor)

    @staticmethod
    def add_game(user_id, game_id):
        cursor = connection.cursor()

        query = 'INSERT INTO user_game (user_id, game_id) VALUES (%s, %s)'
        cursor.execute(query, (user_id, game_id))
        transaction.commit_unless_managed()

    @staticmethod
    def remove_game(user_id, game_id):
        cursor = connection.cursor()

        query = 'DELETE FROM user_game WHERE user_id = %s AND game_id = %s'
        cursor.execute(query, (user_id, game_id))
        transaction.commit_unless_managed()
