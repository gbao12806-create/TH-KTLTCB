print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import math

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    # Khi a = 0 thì phương trình trở thành bậc 1: bx + c = 0
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có một nghiệm duy nhất x =", x)
else:
    # Tính delta
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm (delta < 0).")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)

