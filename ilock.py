from abc import abstractmethod, ABC


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

