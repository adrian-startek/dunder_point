from typing import Dict, Self
import math


class Point2D:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def dot_product(self, other: Self) -> float:
        return self.x * other.x + self.y * other.y

    def vector_sum(self, other: Self) -> Self:
        return Point2D(x=self.x + other.x, y=self.y + other.y)

    def vector_diff(self, other: Self) -> Self:
        return Point2D(x=self.x - other.x, y=self.y - other.y)


if __name__ == "__main__":
    a: Point2D = Point2D(x=3, y=4)
    b: Point2D = Point2D(x=3, y=4)
    c: Point2D = Point2D(x=1, y=1)

    print(f"Our points are: a={a}, b={b}, c={b}")
    print(f"Checking if a == b: {a == b}")
    # print(f"Checking if a < c: {a < c}")

    # values_at_point: Dict[Point2D, int] = {
    #     a: 1,
    #     b: 2,
    #     c: 3
    # }
    #
    # print(values_at_point)

    print("Let's do some type casting: ")
    print(f"\tTo str: {str(a)}")
    print(f"\tTo bool: {bool(a)}")
    # print(f"\tTo int: {int(a)}")
    # print(f"\tTo float: {float(a)}")

    # print(f"Length of the vector a is: {len(a)}")
    print(f"Length of the vector a is: {a.get_length()}")

    # print(f"a + b = {a + b}")
    # print(f"a - b = {a - b}")
    # print(f"a * b = {a * b}")
    # print(f"-a = {-a}")
    # print(f"|a|={abs(a)}")
