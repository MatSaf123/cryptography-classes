from src.database_controller import DatabaseController
from src.utility import Hashing as h
import pytest
import os

if os.path.exists('task-03-database.db'):
    os.remove('task-03-database.db')
dc = DatabaseController()


def test_init_database():
    assert os.path.exists('task-03-database.db') is True


def test_add_user_success():
    dc.add_user('user_01', 'coolpassword')
    user = dc.get_user('user_01')
    assert user[1] == h.hash('coolpassword', user[2])


def test_add_user_already_exists():
    with pytest.raises(AssertionError):
        dc.add_user('user_01', 'coolpassword')


def test_get_all_users():
    assert dc.get_all_users()[0] == dc.get_user('user_01')


def test_get_user_doesnt_exist():
    with pytest.raises(AssertionError):
        dc.get_user('user_02')


def test_delete_user_success():
    dc.delete_user('user_01')
    with pytest.raises(AssertionError):
        dc.get_user('user_01')
