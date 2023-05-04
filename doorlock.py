from ilock import *


class DoorLock(ILock):
    def open(self):
        if self.state:
            print(f'lock already is opened')
            return self.state
        self.state = True
        return self.state

    def close(self):
        if not self.state:
            print(f'already is closed')
            return self.state
        self.state = False
        return self.state


