from django.db.models import Model

class UserGame(Model):

    class Meta:
        managed = False
        db_table = 'user_game'
