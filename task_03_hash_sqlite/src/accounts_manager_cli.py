from database_manager import DatabaseManager
import logging


def register_user() -> None:
    username = InputValidation.read_username()
    password = InputValidation.read_password()

    try:
        dm.add_new_user(username, password)
    except Exception:
        logger.info(' Exception at register_user()')
    finally:
        logger.info(' User registered successfully.')


def display_users() -> None:
    for user in dm.get_all_users():
        print(user)


class InputValidation:
    @staticmethod
    def read_username():
        username = input('Enter your username: ')
        while not dm.get_user(username) == []:
            username = input('Username taken, choose another username: ')
        return username

    @staticmethod
    def read_password():
        password = input('Enter your password: ')
        password_repeated_correctly = (password == input('Repeat your password: '))
        while not password_repeated_correctly:
            password = input('Passwords dont match, try again: ')
            password_repeated_correctly = (password == input('Repeat your password: '))
        return password


if __name__ == '__main__':
    dm = DatabaseManager()
    logger = logging.getLogger('registering')
    logging.basicConfig(level=logging.DEBUG)
    register_user()
    display_users()
