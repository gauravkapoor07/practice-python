class vectors:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        result = vectors(self.x +other.x, self.y +other.y, self.z +other.z)
        return result
    def __mul__(self, other):
        result = self.x*other.x + self.y*other.y + self.z*other.z
        return result
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = vectors(1,2,3)
v2 = vectors(4,5,6)
v3 = vectors(7,8,9)

print(v1+v2) # Output: Vector(5,7,9,)
print(v1 * v2) # Output : 32

print(v1 + v3)
print(v1*v3)
