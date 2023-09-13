from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @abstractmethod
    def is_valid(self):
        raise NotImplementedError

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure.__class__.__name__} is not a figure.")
        return round(self.area + figure.area, 5)
