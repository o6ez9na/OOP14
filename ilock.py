from abc import abstractmethod, ABC

password = '123'


class ILock(ABC):
    def __init__(self, key: str):
        self.key = key
        self.state = False

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass
