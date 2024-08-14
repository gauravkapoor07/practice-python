class vectors:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return 3  # Assuming vectors are 3D for this method to work correctly.

# Test the implementation
v1 = vectors(1,2,3)
v2 = vectors(4,5,6)
v3 = vectors(7,8,9)

print(len(v1))
print(len(v2))
print(len(v3))
