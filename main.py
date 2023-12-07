class Vector:
    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, (list, tuple)):
            self.x, self.y, self.z = x
        else:
            self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def length(self):
        return abs(self)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vector_product(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    @staticmethod
    def triple_product(a, b, c):
        return a.scalar_product(b.vector_product(c))

    def __xor__(self, other):
        return self.vector_product(other)

    def __or__(self, other):
        return abs(self.vector_product(other)) == 0

    @staticmethod
    def are_complanar(a, b, c):
        return (a ^ b) | c

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)
print(v1 + v2)
print(v1 - v2)
print(-v1)
print(v1 * 2)
print(v1.scalar_product(v2))
print(v1 ^ v2)
print(v1 | v3)
print(Vector.are_complanar(v1, v2, v3))