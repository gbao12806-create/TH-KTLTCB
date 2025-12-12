print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
r = float(input("Nhập bán kính hình tròn: "))
c = Circle(r)
print("Diện tích hình tròn là:", c.area())
print("Chu vi hình tròn là:", c.perimeter())

