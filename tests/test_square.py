import pytest

from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("side", "area", "perimeter"),
    [
        (1, 1, 4),
        (0.01, 0.0001, 0.04),
    ],
)
def test_square_create_positive(side, area, perimeter):
    square = Square(side)

    assert square.name == f"Square ({side=})"
    assert square.area == area
    assert square.perimeter == perimeter


@pytest.mark.parametrize(
    "side",
    [
        0,
        -0.001,
        "1",
        True,
    ],
)
def test_square_create_negative(side):
    with pytest.raises(ValueError):
        Square(side)


def test_square_add_area():
    square_1 = Square(2)
    square_2 = Square(5)
    rectangle = Rectangle(2, 5)
    circle = Circle(5)
    triangle = Triangle(2, 2, 3)

    assert square_1.add_area(square_1) == 8
    assert square_1.add_area(square_2) == 29
    assert square_1.add_area(rectangle) == 14
    assert square_1.add_area(circle) == 82.53982
    assert square_1.add_area(triangle) == 5.98431


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
def test_square_add_area_negative(some_object):
    square = Square(7)

    with pytest.raises(ValueError):
        square.add_area(some_object)
