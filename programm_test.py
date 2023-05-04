import pytest
from main import *


@pytest.fixture
def password_len():
    return len(password)


@pytest.fixture
def password_text():
    return password


@pytest.fixture
def door_state():
    return door.state


@pytest.fixture
def lock_state():
    return lock.state


def test_max_len_password(password_len):
    assert password_len <= 16, f'{password_len} should be < 16'


def test_min_len_password(password_len):
    assert password_len >= 3, f'{password_len} should be >3'


def test_current_symbol_password(password_text):
    assert password_text != ' ', f'Password is incorrect'


def test_value_password(password_text):
    assert password_text != 'e', f'Password cant be "e"'


def test_door_lock_state(lock_state, door_state):
    assert lock_state == door_state, 'Door and lock bug'


def test_password_reset(lock_state, door_state):
    if door_state:
        assert lock.reset_password()


def test_close_door(door_state, lock_state):
    if door_state:
        door.close()
        assert not door_state and not lock_state


def test_open_door(door_state, lock_state):
    if not door_state:
        door.open()
        assert not(door_state and lock_state)
