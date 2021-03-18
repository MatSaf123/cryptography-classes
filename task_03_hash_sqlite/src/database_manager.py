import sqlite3
import os
from models.user import User


class DatabaseManager:
    """This class manages all database CRUD operations."""

    DATABASE_PATHNAME = 'task-03-database.db'

    def __init__(self):
        """Initializes DatabaseManager. If database file doesn't exist,
        creates one."""

        if not os.path.exists(self.DATABASE_PATHNAME):
            self.__initialize_database()

    def __connect_with_db(self) -> sqlite3.Connection:
        """Opens up connection with sqlite database.

        :return: SQLite database connection object
        :rtype: sqlite3.Connection
        """

        try:
            return sqlite3.connect(self.DATABASE_PATHNAME)
        except sqlite3.Error:
            raise sqlite3.Error

    def __initialize_database(self) -> bool:
        """Creates new database within given pathname (hardcoded above).
        If a database already exists in that place, it's replaced
        by a new, empty one.

        :return: True if successfully created database, False if didn't.
        :rtype: bool
        """

        if os.path.isfile(self.DATABASE_PATHNAME):
            os.remove(self.DATABASE_PATHNAME)

        conn = sqlite3.connect(self.DATABASE_PATHNAME)
        c = conn.cursor()
        c.execute("""CREATE TABLE users (
                    username text,
                    password text,
                    salt text
                    )""")
        conn.commit()
        conn.close()
        return True

    def add_new_user(self, username: str, password: str) -> bool:
        """Adds new user to database.

        :param username: username for given user
        :type username: str
        :param password: password that is about to be hashed
        :type password: str
        :return: True if successfully added new user, False if didn't
        :rtype: bool
        """

        assert self.get_user(username) == [], 'Provided username is already in use.'

        conn = self.__connect_with_db()
        c = conn.cursor()
        user = User(username, password)

        c.execute("INSERT INTO users VALUES ("
                  ":username,"
                  " :password,"
                  " :salt)",
                  {'username': user.username,
                   'password': user.password,
                   'salt': user.salt})
        conn.commit()
        conn.close()
        return True

    def get_user(self, username: str) -> list:
        """Fetches a record from db with that contains provided username.

        :param username: username for given user
        :type username: str
        :return: list containing given user's data
        :rtype: list
        """

        conn = self.__connect_with_db()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = :username", {'username': username})
        user = c.fetchall()
        conn.close()
        return user

    def delete_user(self, username: str) -> bool:
        """Removes user from database.

                :param username: username of user that is about to get removed from db
                :type username: str
                :return: True if successfully added new user, False if didn't
                :rtype: bool
                """

        conn = self.__connect_with_db()
        c = conn.cursor()

        assert self.get_user(username) != [], 'There is no such user in database.'

        c.execute("DELETE FROM users WHERE username = :username", {'username': username})
        conn.commit()
        conn.close()
        return True

    def get_all_users(self) -> list:
        """Fetches all records from db (only for testing purposes).

        :return: list of all records from db
        :rtype: list
        """
        conn = self.__connect_with_db()
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users

