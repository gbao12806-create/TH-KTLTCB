print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

n = int(input("Nhap n: "))
for i in range(1, n):
tong = sum([j for j in range(1, i) if i % j == 0])
if tong > i:
print(i)

