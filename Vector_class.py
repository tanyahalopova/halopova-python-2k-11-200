class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, MyVector):
            return MyVector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("аргумент должен быть вектором")

    def __sub__(self, other):
        if isinstance(other, MyVector):
            return MyVector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("ргумент должен быть вектором")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("аргумент должен быть числом")

    def __str__(self):
        return f"({self.x}, {self.y})"


a = MyVector(2, 3)
b = MyVector(3, 4)

result = a + b
print(result)

result = a - b
print(result)