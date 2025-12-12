print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

tong = 0
print("Nhap cac giao dich (D/W so_tien), nhap rong de ket thuc:")
while True:
s = input()
if not s:
break
t, v = s.split()
v = int(v)
if t == 'D':
tong += v
elif t == 'W':
tong -= v
print(tong)

