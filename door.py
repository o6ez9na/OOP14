from ilock import ILock


class Door:
    def __init__(self, lock: ILock):
        self.lock = lock
        self.state = False

    def open(self):
        if self.lock.open():
            return self.state
        self.lock.open()
        self.state = True
        return self.state

    def close(self):
        if not self.lock.close():
            return self.state
        self.lock.close()
        self.state = False
        return self.state

    def reset_password(self, key_code):
        if self.state:
            self.lock.key = key_code
        return self.lock.key
