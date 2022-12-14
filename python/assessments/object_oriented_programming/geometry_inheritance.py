import math


class Polygon:
    def get_area(self):
        raise NotImplementedError()

    def get_sides(self):
        raise NotImplementedError()

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    def get_sides(self):
        return self.sides

    def get_area(self):
        side1, side2, side3 = self.sides
        return self.get_triangle_area(side1, side2, side3)

    # Use this function in your solution.
    @staticmethod
    def get_triangle_area(side1, side2, side3):
        semi_perimeter = (side1 + side2 + side3) / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - side1) *
            (semi_perimeter - side2) *
            (semi_perimeter - side3)
        )


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]

    def get_area(self):
        return self.get_rectangle_area(self.width, self.height)

    # Use this function in your solution.
    @staticmethod
    def get_rectangle_area(width, height):
        return width * height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)