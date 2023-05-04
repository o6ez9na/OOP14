from abc import abstractmethod, ABC

code = '123'


class Lock(ABC):
    def __init__(self, key=None):
        self.key = key
        self.is_open = False

    @abstractmethod
    def open(self, key_code):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def check_code(self, key_code):
        pass
