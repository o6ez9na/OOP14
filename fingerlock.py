from ilock import *


class FingerLock(ILock):
    def open(self):
        if self.state:
            print(f'lock already is opened')
            return self.state
        # a = input(f'input password: ')
        a = '123'
        if a != self.key:
            print(f'password {a} is incorrect')
            return self.state
        self.state = True
        return self.state

    def close(self):
        if not self.state:
            print(f'already is closed')
            return self.state
        self.state = False
        return self.state

    def reset_password(self):
        if self.state:
            self.key = '777'
        return self.key
