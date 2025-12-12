print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import math

x1 = float(input("Enter x1 ---> "))
y1 = float(input("Enter y1 ---> "))

x2 = float(input("Enter x2 ---> "))
y2 = float(input("Enter y2 ---> "))

d1 = (x2 - x1) ** 2
d2 = (y2 - y1) ** 2
res = math.sqrt(d1 + d2)

print("Distance between two points:", res)
