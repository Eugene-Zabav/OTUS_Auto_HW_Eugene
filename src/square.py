from src.figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__(f"Square ({side=})")
        self.side = side

        self.is_valid()

    def is_valid(self):
        # Type validation.
        if not isinstance(self.side, int | float) or isinstance(self.side, bool):
            raise ValueError("Only int or float")

        # Positive value validation.
        if self.side <= 0:
            raise ValueError("Only positive numbers")

    @property
    def area(self):
        return round(self.side**2, 5)

    @property
    def perimeter(self):
        return round(self.side * 4, 5)
