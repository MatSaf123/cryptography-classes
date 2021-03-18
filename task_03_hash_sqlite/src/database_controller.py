import sqlite3
import os
from models.user import User


class DatabaseController:
    """Handles database connections and CRUD operations."""

    DATABASE_PATHNAME = 'task-03-database.db'

    def __init__(self):
        """Creates new database within given pathname (hardcoded above)."""

        if not os.path.exists(self.DATABASE_PATHNAME):
            conn = sqlite3.connect(self.DATABASE_PATHNAME)
            c = conn.cursor()
            c.execute("""CREATE TABLE users (
                        username text,
                        password text,
                        salt text
                        )""")
            conn.commit()
            conn.close()

    def __connect_with_db(self) -> sqlite3.Connection:
        """Opens up connection with sqlite database.

        :return: SQLite database connection object
        :rtype: sqlite3.Connection
        """

        try:
            return sqlite3.connect(self.DATABASE_PATHNAME)
        except sqlite3.Error:
            raise sqlite3.Error

    def add_user(self, username: str, password: str) -> None:
        """Adds new user to database.

        :param username: username for given user
        :type username: str
        :param password: password that is about to be hashed
        :type password: str
        """

        assert self.get_user(username) is None, 'Provided username is already in use.'

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

    def delete_user(self, username: str) -> None:
        """Removes user from database.

        :param username: username of user that is about to get removed from db
        :type username: str
        """

        conn = self.__connect_with_db()
        c = conn.cursor()

        assert self.get_user(username) != [], 'There is no such user in database.'

        c.execute("DELETE FROM users WHERE username = :username", {'username': username})
        conn.commit()
        conn.close()

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
        user = c.fetchone()

        # assert user is not None, 'There is no user name as provided.'

        conn.close()
        return user

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
