from copy import copy

from lock import Lock


class Door:
    def __init__(self, lock: Lock = None):
        self.lock = lock
        self.is_open = False

    def open(self, key_code=None):
        if self.lock is None:
            self.is_open = True
            return self.is_open
        else:
            if key_code is None:
                raise AttributeError
            if self.lock.is_open:
                return self.is_open
            if self.lock.open(key_code):
                self.is_open = True
                return self.is_open

    def close(self):
        if self.lock is None:
            self.is_open = False
            return self.is_open
        else:
            if not self.lock.is_open:
                return self.is_open
            self.lock.close()
            self.is_open = False
            return self.is_open

    def change_password(self, key_code):
        if self.is_open:
            self.lock.key = copy(key_code)
