from door import *
from fingerlock import *

password = '123'
lock = FingerLock(password)
door = Door(lock)
door.open()
lock.reset_password()
door.close()

