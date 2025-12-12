print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

import re

value = []
items = [x for x in input("Nhập danh sách mật khẩu (ngăn cách bằng dấu phẩy): ").split(',')]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[$#@]", p):
        continue
    if re.search("\s", p):  # không cho phép khoảng trắng
        continue
    value.append(p)

print(",".join(value))

