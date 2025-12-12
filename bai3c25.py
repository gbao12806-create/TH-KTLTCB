print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

lst = list(map(int, input("Nhap danh sach so, cach nhau boi dau phay: ").split(',')))
res = [x for x in lst if x % 2 == 1]
print(res)

