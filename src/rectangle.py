from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__(f"Rectangle ({length=}, {width=})")
        self.length = length
        self.width = width

        self.is_valid()

    def is_valid(self):
        # Type validation.
        if (
            not isinstance(self.length, int | float)
            or not isinstance(self.width, int | float)
            or isinstance(self.length, bool)
            or isinstance(self.width, bool)
        ):
            raise ValueError("Only int or float")

        # Positive value validation.
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Only numbers")

    @property
    def area(self):
        return round(self.length * self.width, 5)

    @property
    def perimeter(self):
        return round((self.length + self.width) * 2, 5)
