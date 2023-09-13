import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(f"Circle ({radius=})")
        self.radius = radius

        self.is_valid()

    def is_valid(self):
        # Type validation.
        if not isinstance(self.radius, int | float) or isinstance(self.radius, bool):
            raise ValueError("Only int or float")

        # Positive value validation.
        if self.radius <= 0:
            raise ValueError("Only positive numbers")

    @property
    def area(self):
        return round(math.pi * self.radius**2, 5)

    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 5)
