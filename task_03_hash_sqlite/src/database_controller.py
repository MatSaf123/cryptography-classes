import sqlite3
import os
from src.models.user import User


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
        except sqlite3.Error as e:
            raise sqlite3.Error

    def add_user(self, username: str, password: str) -> None:
        """Adds new user to database.

        :param username: username for given user
        :type username: str
        :param password: password that is about to be hashed
        :type password: str
        """

        assert not self.user_exists_in_database(username), 'User with that username already exists.'

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

        try:
            self.get_user(username)
        except AssertionError:
            raise ValueError('There is no user with provided username.')

        conn = self.__connect_with_db()
        c = conn.cursor()
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
        conn.close()

        assert user is not None, 'There is no user with provided username.'

        return user

    def user_exists_in_database(self, username: str) -> bool:
        """Checks if user with given name exists in the database.

        :param username: username for given user
        :type username: str
        :return: True if user exists, False if not
        :rtype: bool
        """

        try:
            self.get_user(username)
        except AssertionError:
            return False
        else:
            return True

    def get_all_users(self) -> list:
        """Fetches all records from db.

        :return: list of all records from db
        :rtype: list
        """

        conn = self.__connect_with_db()
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users
