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
    reset_code = '777'
    lock = FingerLock(code)
    assert not lock.state
    door = Door(lock)
    assert not door.state
    door.lock.check_code(reset_code)
    assert door.lock.state
    door.open()
    assert door.state == True and lock.state == True
    door.reset_password(reset_code)
    assert door.lock.key == reset_code
    door.close()
    assert door.state == False and lock.state == False
