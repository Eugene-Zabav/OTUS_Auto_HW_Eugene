import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("length", "width", "area", "perimeter"),
    [
        (1, 2, 2, 6),
        (0.01, 0.01, 0.0001, 0.04),
    ],
    ids=[
        "integers",
        "fractional"
    ]
)
def test_rectangle_create_positive(length, width, area, perimeter):
    rectangle = Rectangle(length, width)

    assert rectangle.name == f"Rectangle ({length=}, {width=})"
    assert rectangle.area == area
    assert rectangle.perimeter == perimeter


@pytest.mark.parametrize(
    ("length", "width"),
    [
        (0, 2),
        (-0.001, 2),
        ("1", 2),
        (True, 2),
        (None, 2),
        (2, 0),
        (2, -0.001),
        (2, "1"),
        (2, True),
        (2, None),
    ],
    ids=[
        "length-zero",
        "length-negative",
        "length-string",
        "length-bool",
        "length-None",
        "width-zero",
        "width-negative",
        "width-string",
        "width-bool",
        "width-None",
    ]
)
def test_rectangle_create_negative(length, width):
    with pytest.raises(ValueError):
        Rectangle(length, width)


def test_rectangle_add_area():
    rectangle_1 = Rectangle(2, 5)
    rectangle_2 = Rectangle(1, 3)
    square = Square(5)
    circle = Circle(5)
    triangle = Triangle(3, 3, 3)

    assert rectangle_1.add_area(rectangle_1) == 20
    assert rectangle_1.add_area(rectangle_2) == 13
    assert rectangle_1.add_area(square) == 35
    assert rectangle_1.add_area(circle) == 88.53982
    assert rectangle_1.add_area(triangle) == 13.89711


@pytest.mark.parametrize(
    "some_object",
    [
        1,
        1.5,
        "string",
        True,
        None,
    ],
    ids=[
        "int",
        "float",
        "string",
        "bool",
        "None"
    ]
)
def test_rectangle_add_area_negative(some_object):
    rectangle = Rectangle(2, 5)

    with pytest.raises(ValueError):
        rectangle.add_area(some_object)
