from database_manager import DatabaseManager
import logging


def register_user() -> None:
    """Adds user (his username and hashed password) to the database."""

    username = InputValidation.read_username()
    password = InputValidation.read_password()
    dm.add_user(username, password)
    logger.info('Account registered.')


def display_users() -> None:
    """Displays all user data from database."""

    for user in dm.get_all_users():
        logger.info(user)


# TODO: log-in functionality

class InputValidation:
    """User input validation functionality."""

    @staticmethod
    def read_username() -> str:
        """Read user input and return unique (not existing in db) username.

        :return: unique username chosen by user
        :rtype: str
        """

        logger.info('Enter username: ')
        username = input()
        while not dm.get_user(username) == []:
            logger.info('Username taken, choose another username:')
            username = input()
        return username

    @staticmethod
    def read_password() -> str:
        """Read user input and return verified (repeated correctly) username.

        :return: password
        :rtype: str
        """

        logger.info('Enter your password: ')
        password = input()
        logger.info('Repeat your password: ')
        password_repeated_correctly = (password == input())
        while not password_repeated_correctly:
            logger.info('Passwords dont match, try again: ')
            password = input()
            logger.info('Repeat your password: ')
            password_repeated_correctly = (password == input())
        return password


if __name__ == '__main__':
    dm = DatabaseManager()
    logger = logging.getLogger('registering')
    logging.basicConfig(level=logging.DEBUG)
    register_user()
    display_users()

# TODO: write some better CLI
