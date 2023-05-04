from lock import *


class FingerLock(Lock):
    def open(self, key_code):
        if key_code is None:
            self.is_open = True
            return self.is_open
        else:
            if self.is_open:
                print(f'lock already is opened')
                return self.is_open
            if self.check_code(key_code):
                self.is_open = True
                return self.is_open

    def close(self):
        if self.key is None:
            self.is_open = False
            return self.is_open
        else:
            if not self.is_open:
                print(f'already is closed')
                return self.is_open
            self.is_open = False
            return self.is_open

    def check_code(self, key_code):
        if self.key != key_code:
            print(f'password {key_code} is incorrect')
            return False
        return True
