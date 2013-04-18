from django.db import models, connection, transaction

from game_atlas.utils.models import dict_fetch_all, dict_fetch_one

class Friends(models.Model):

    class Meta:
        managed = False
        db_table = 'friend'
    #This will be used to send a friend request message (type_id of 0)
    @staticmethod
    def get_userid(username):
        cursor = connection.cursor()

        query = 'SELECT id from auth_user where username = %s'
        cursor.execute(query, (username))

        return dict_fetch_one(cursor)

    @staticmethod
    def add_friends(user1, user2):
        cursor = connection.cursor()

        query = 'INSERT INTO friend (user_id, friend_id) VALUES (%s, %s)'
        cursor.execute(query, (user1, user2))
        transaction.commit_unless_managed()

    @staticmethod
    def accept_friends(user1, user2):
        cursor = connection.cursor()

        query = 'INSERT INTO friend (user_id, friend_id) VALUES (%s, %s)'
        cursor.execute(query, (user1, user2))
        transaction.commit_unless_managed()

    @staticmethod
    def reject_friend(user1, user2):
        cursor =connection.cursor()

        query = 'DELETE FROM friend WHERE user_id = %s AND friend_id = %s'
        cursor.execute(query, (user2, user1))
        transaction.commit_unless_managed()

    #Removes from both users friends list
    @staticmethod
    def remove_friends(user1, user2):
        cursor = connection.cursor()

        query = 'DELETE FROM friend WHERE user_id = %s AND friend_id = %s'
        cursor.execute(query, (user1, user2))
        cursor.execute(query, (user2, user1))
        transaction.commit_unless_managed()

    #Returns all the friends of a user as long as the friendship has been accepted. 
    @staticmethod
    def get_friends(user_id):
        cursor = connection.cursor()
        #We probably need to fix this query up a little bit since its not a symmetric relationship
        query = 'SELECT username, id FROM friend INNER JOIN auth_user ON friend_id = id WHERE user_id = %s'
        cursor.execute(query, (user_id,))
        
        return dict_fetch_all(cursor)
    @staticmethod
    def find_user(user_id):
        cursor = connection.cursor()

        query = 'SELECT username FROM auth_user WHERE id=%s'
        cursor.execute(query, (user_id))

        return dict_fetch_one(cursor)
