import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area", "perimeter"),
    [
        (3, 4, 5, 6, 12),
        (0.9, 0.9, 0.9, 0.35074, 2.7),
    ],
)
def test_rectangle_create_positive(side_a, side_b, side_c, area, perimeter):
    triangle = Triangle(side_a, side_b, side_c)

    assert triangle.name == f"Triangle ({side_a=}, {side_b=}, {side_c=})"
    assert triangle.area == area
    assert triangle.perimeter == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (0, 2, 3),
        (-0.001, 2, 3),
        ("1", 2, 3),
        (True, 2, 3),
        (2, 0, 3),
        (2, -0.001, 3),
        (2, "1", 3),
        (2, True, 3),
        (2, 3, 0),
        (2, 3, -0.001),
        (2, 3, "1"),
        (2, 3, True),
        (1, 1, 2),
        (1, 2, 1),
        (2, 1, 1),
        (1, 1, 3),
        (1, 3, 1),
        (3, 1, 1),
    ],
)
def test_triangle_create_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_add_area():
    triangle_1 = Triangle(2, 2, 2)
    triangle_2 = Triangle(4, 5, 5)
    rectangle = Rectangle(2, 5)
    square = Square(5)
    circle = Circle(5)

    assert triangle_1.add_area(triangle_1) == 3.4641
    assert triangle_1.add_area(triangle_2) == 10.8972
    assert triangle_1.add_area(rectangle) == 11.73205
    assert triangle_1.add_area(square) == 26.73205
    assert triangle_1.add_area(circle) == 80.27187


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
def test_triangle_add_area_negative(some_object):
    triangle = Triangle(2, 5, 4)

    with pytest.raises(ValueError):
        triangle.add_area(some_object)
