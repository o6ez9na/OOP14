from door import *
password = '123'
new_password = '777'

door = Door()
door.open()

if door.is_open:
    print('ready')