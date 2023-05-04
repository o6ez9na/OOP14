from door import *
from fingerlock import *
password = '123'
new_password = '777'

lock = FingerLock(password)
door = Door(lock)
door.open(password)
