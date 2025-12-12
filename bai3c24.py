print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

s = input("Nhap cau: ")
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)
print("Chu hoa:", upper)
print("Chu thuong:", lower)

