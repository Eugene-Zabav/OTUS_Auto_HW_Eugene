from figure import Square, Triangle, Circle, Rectangle


def main():
    square = Square(10)
    triangle = Triangle(13, 14, 15)
    circle = Circle(5)
    rectangle = Rectangle(5, 10)

    print("triangle.area = ", triangle.area)
    print("square.area = ", square.area)
    print("triangle.add_area(square) = ", triangle.add_area(square))
    print("circle.area = ", circle.area)
    print("rectangle.area = ", rectangle.area)


if __name__ == "__main__":
    main()
