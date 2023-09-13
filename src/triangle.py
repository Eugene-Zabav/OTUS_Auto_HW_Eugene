from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(f"Triangle ({side_a=}, {side_b=}, {side_c=})")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        self.is_valid()

    def is_valid(self):
        # Type validation.
        if (
            not isinstance(self.side_a, int | float)
            or not isinstance(self.side_b, int | float)
            or not isinstance(self.side_c, int | float)
            or isinstance(self.side_a, bool)
            or isinstance(self.side_b, bool)
            or isinstance(self.side_c, bool)
        ):
            raise ValueError("Only int or float")

        # Positive value validation.
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Only positive numbers")

        # Triangle possibility validation.
        if (
            (self.side_a + self.side_b <= self.side_c)
            or (self.side_a + self.side_c <= self.side_b)
            or (self.side_b + self.side_c <= self.side_a)
        ):
            raise ValueError("Invalid triangle")

    @property
    def area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return round(
            (
                (
                    semi_perimeter
                    * (semi_perimeter - self.side_a)
                    * (semi_perimeter - self.side_b)
                    * (semi_perimeter - self.side_c)
                )
                ** 0.5
            ),
            5,
        )

    @property
    def perimeter(self):
        return round(self.side_a + self.side_b + self.side_c, 5)
