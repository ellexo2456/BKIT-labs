from abc import ABC, abstractmethod


class Figure(ABC):
    FIGURE_TYPE = None

    @classmethod
    def type(cls):
        return cls.FIGURE_TYPE

    @abstractmethod
    def square(self):
        pass
