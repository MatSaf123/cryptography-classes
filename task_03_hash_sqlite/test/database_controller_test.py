from task_03_hash_sqlite.src.database_controller import DatabaseController
from task_03_hash_sqlite.src.utility import Hashing as h
import pytest
import os

if os.path.exists('task-03-database.db'):
    os.remove('task-03-database.db')
dm = DatabaseController()


def test_init_database():
    assert os.path.exists('task-03-database.db') is True


def test_add_user_success():
    dm.add_user('user_01', 'coolpassword')
    user = dm.get_user('user_01')
    assert user[1] == h.encrypt('coolpassword', user[2])


def test_add_user_already_exists():
    with pytest.raises(Exception):
        dm.add_user('user_01', 'coolpassword')


def test_get_all_users():
    assert dm.get_all_users()[0] == dm.get_user('user_01')


def test_get_user_doesnt_exist():
    assert dm.get_user('user_02') is None


def test_delete_user_success():
    dm.delete_user('user_01')
    assert dm.get_user('user_01') is None
