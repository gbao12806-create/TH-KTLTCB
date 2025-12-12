lst = list(map(int, input("Nhap danh sach so, cach nhau boi dau phay: ").split(',')))
res = [x for x in lst if x % 2 == 1]
print(res)
