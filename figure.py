class Figure:
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        raise NotImplementedError

    @property
    def perimeter(self):
        raise NotImplementedError

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError(f"{figure.__class__.__name__} is not a figure.")


class Square(Figure):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length + self.width) * 2


class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def perimeter(self):
        return 6.28 * self.radius


class Triangle(Figure):
    def __init__(
        self,
        side_a,
        side_b,
        side_c,
    ):
        super().__init__("Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise ValueError(
                "Invalid triangle. One side of the triangle is equal to "
                "or greater than the sum of the other two sides."
            )

    def is_valid(self):
        return (
            (self.side_a + self.side_b > self.side_c)
            and (self.side_a + self.side_c > self.side_b)
            and (self.side_b + self.side_c > self.side_a)
        )

    @property
    def area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return (
            semi_perimeter
            * (semi_perimeter - self.side_a)
            * (semi_perimeter - self.side_b)
            * (semi_perimeter - self.side_c)
        ) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
