from database_manager import DatabaseManager
from utility import Verification as vf
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


def log_in() -> None:
    """Verifies login and password, simulates logging in with given credentials."""

    logger.info('Enter your username:')
    username = input()
    logger.info('Enter your password:')
    password = input()
    account = dm.get_user(username)

    if not account:
        logger.info('No account with given username found.')
        return

    if vf.check_if_passwords_are_the_same(password, account):
        logger.info('Successfully logged in.')
    else:
        logger.info('Wrong password, try again.')


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
        assert len(username) > 0, 'Username cannot be empty.'

        while dm.get_user(username) is not None:
            logger.info('Username taken, choose another username:')
            username = input()
        return username

    @staticmethod
    def read_password() -> str:
        """Read user input and return validated (repeated correctly by user) password.

        :return: password
        :rtype: str
        """

        logger.info('Enter your password: ')
        password = input()
        assert len(password) > 0, 'Password cannot be empty.'
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
    # display_users()
    log_in()

# TODO: write some better CLI :D
