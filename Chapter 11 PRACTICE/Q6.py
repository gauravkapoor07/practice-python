class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

v = vector(7, 8, 10)
print(v)