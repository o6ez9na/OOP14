from ilock import *


class FingerLock(ILock):
    def open(self, key_code):
        if self.state:
            print(f'lock already is opened')
            return self.state
        self.check_code(key_code)
        self.state = True
        return self.state

    def close(self):
        if not self.state:
            print(f'already is closed')
            return self.state
        self.state = False
        return self.state

    def check_code(self, key_code):
        if self.key != key_code:
            print(f'password {key_code} is incorrect')
            return self.state
