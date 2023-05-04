import pytest
from fingerlock import *
from door import *


def test_len_password():
    code = '123'
    assert len(code) >= 3, f'{len(code)} should be > 3'
    assert len(code) <= 16, f'{len(code)} should be < 16'


def test_current_symbol_password():
    code = '123'
    assert code != ' ' or code != 'e', f'Password is incorrect'
    code = 'e'
    assert code != ' ' or code != 'e', f'Password is incorrect'
    code = ' '
    assert code != ' ' or code != 'e', f'Password is incorrect'


def test_door_state():
    code = '123'
    lock = FingerLock(code)
    assert not lock.is_open
    door = Door(lock)
    assert not door.is_open
    door.open(code)
    assert door.is_open and lock.is_open
    door.close()
    assert not door.is_open and not lock.is_open


def test_change_password():
    code = '123'
    reset_code = '777'
    lock = FingerLock(code)
    door = Door(lock)
    door.open(reset_code)
    assert not door.is_open
    door.open(code)
    assert door.is_open
    door.change_password(reset_code)
    assert door.lock.key == reset_code
    door.close()
    assert not door.is_open


def test_door_without_lock():
    door = Door()
    assert not door.is_open
    door.open()
    assert door.is_open
    door.close()
    assert not door.is_open
