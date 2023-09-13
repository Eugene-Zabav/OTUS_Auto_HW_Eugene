import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("radius", "area", "perimeter"),
    [
        (1, 3.14159, 6.28319),
        (0.01, 0.00031, 0.06283),
    ],
)
def test_circle_create_positive(radius, area, perimeter):
    circle = Circle(radius)

    assert circle.name == f"Circle ({radius=})"
    assert circle.area == area
    assert circle.perimeter == perimeter


@pytest.mark.parametrize(
    "radius",
    [
        0,
        -0.001,
        "1",
        True,
        None,
    ],
)
def test_circle_create_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_add_area():
    circle_1 = Circle(2)
    circle_2 = Circle(3)
    square = Square(1)
    rectangle = Rectangle(1, 3)
    triangle = Triangle(2, 3, 4)

    assert circle_1.add_area(circle_1) == 25.13274
    assert circle_1.add_area(circle_2) == 40.8407
    assert circle_1.add_area(square) == 13.56637
    assert circle_1.add_area(rectangle) == 15.56637
    assert circle_1.add_area(triangle) == 15.47111


@pytest.mark.parametrize(
    "some_object",
    [
        1,
        1.5,
        "string",
        True,
        None,
    ],
)
def test_circle_add_area_negative(some_object):
    circle = Circle(7)

    with pytest.raises(ValueError):
        circle.add_area(some_object)
