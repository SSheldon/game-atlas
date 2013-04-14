from django.db import models, connection, transaction

class Friends(models.Model):

    class Meta:
        managed = False
        db_table = 'friends'

    def dict_fetch_all(cursor):
        """Return all rows from a cursor as a dict"""
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    #adds friends to the database once both of them agree to be friends
    @staticmethod
    def add_friends(user1, user2):
        cursor = connection.cursor()

        query = 'INSERT INTO friends (user_id, friend_id) VALUES (%s, %s)'
        cursor.execute(query, (user1, user2))
        cursor.execute(query, (user2, user1))
        transaction.commit_unless_managed()

    #Removes from both users friends list
    @staticmethod
    def remove_friends(user1, user2):
        cursor = connection.cursor()

        query = 'DELETE FROM friends WHERE user_id = %s AND friend_id = %s'
        cursor.execute(query, (user1, user2))
        cursor.execute(query, (user2, user1))
        transaction.commit_unless_managed()

    #Returns all the friends of a user as long as the friendship has been accepted. 
    @staticmethod
    def get_friends(user_id):
        cursor = connection.cursor()
        #We probably need to fix this query up a little bit since its not a symmetric relationship
        query = 'SELECT username FROM friends INNER JOIN auth_user ON friend_id = id WHERE user_id = %s'
        cursor.execute(query, (user_id))
        
        return dict_fetch_all(cursor)
    @staticmethod
    def find_user(user_id):
        cursor = connection.cursor()

        query = 'SELECT username FROM auth_user WHERE id=%s'
        cursor.execute(query, (user_id))

        row = cursor.fetchone()
        if not row:
            return {}
        return dict(zip((col[0] for col in cursor.description), row))