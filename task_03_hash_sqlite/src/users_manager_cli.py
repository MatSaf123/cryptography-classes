from database_controller import DatabaseController
from utility import Hashing as h
import logging
import sys


class Manager:
    """All program-user interactions and operations handling."""

    logger = logging.getLogger('manager')
    logging.basicConfig(level=logging.INFO)

    def __init__(self):
        self.dc = DatabaseController()

    def read_username(self) -> str:
        """Read username and check in database if it's unique.

        :return: user username
        :rtype: str
        """

        self.logger.info('Enter username (3 characters length min.): ')
        username = input()
        while self.dc.user_exists_in_database(username) or len(username) < 3:
            self.logger.info('Username taken or invalid, choose another username (3 characters length min.):')
            username = input()
        return username

    def read_password(self) -> str:
        """Read and make user confirm his password.

        :return: user password
        :rtype: str
        """

        self.logger.info('Enter your password (3 characters length min.): ')
        password = input()
        self.logger.info('Repeat your password: ')
        while (password != input()) or len(password) < 3:
            self.logger.info('Invalid password, try again (3 characters length min.): ')
            password = input()
            self.logger.info('Repeat your password: ')
        return password

    def add_user(self) -> None:
        """Takes input from user (his username and password) and attempts to add it to the database."""

        username = self.read_username()
        password = self.read_password()
        try:
            self.dc.add_user(username, password)
        except AssertionError as ae:
            self.logger.info("Didn't add user.")
            self.logger.info(type(ae))
            self.logger.info(ae)
        else:
            self.logger.info('User added.')

    def show_users(self) -> None:
        """Displays all user data from database."""

        for user in self.dc.get_all_users():
            self.logger.info(user)

    def log_in(self) -> bool:
        """Verifies login and password, simulates logging in with given credentials.

        :return: True if logged in, False if not
        :rtype: bool
        """

        self.logger.info('Enter your username:')
        username = input()
        self.logger.info('Enter your password:')
        password = input()
        try:
            user = self.dc.get_user(username)
        except AssertionError:
            self.logger.info('No account with given username found.')
            return False
        else:
            if h.check_if_hashed_passwords_match(password, user):
                self.logger.info('Successfully logged in.')
                return True
            else:
                self.logger.info('Wrong password, try to log in again.')
                return False

    def delete_user(self) -> None:
        """Deletes user from database."""

        self.logger.info('Enter username of user you want to be deleted:')
        username = input()
        try:
            self.dc.delete_user(username)
        except ValueError as e:
            self.logger.info('There is no user with that username.')
        else:
            self.logger.info('User deleted.')


if __name__ == '__main__':
    '''Main module.
    
    Flags for functionalities:
    -a      register new user
    -d      delete user
    -s      show all users
    -l      log in
    -h      help commands
    '''

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    m = Manager()

    if "-a" in opts:
        m.add_user()
    elif "-d" in opts:
        m.delete_user()
    elif "-s" in opts:
        m.show_users()
    elif "-l" in opts:
        m.log_in()
    elif "-h" in opts:
        m.logger.info(f"Flags for functionalities:"
                      f"\n-a      add new user"
                      f"\n-d      delete user"
                      f"\n-s      show all users"
                      f"\n-l      log in"
                      f"\n-h      help commands")
    else:
        raise SystemExit(f"Usage of this script: {sys.argv[0]} -r | -d | -s | -l | -h (type -h for help)")
