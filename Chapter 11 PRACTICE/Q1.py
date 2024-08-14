class two_D_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")
class three_D_vector(two_D_vector):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")

a = two_D_vector(1,2)
a.show()
v  = three_D_vector(5,2,3)
v.show()
