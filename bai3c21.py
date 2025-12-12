lst = input("Nhap cac so nhi phan 4 chu so, cach boi dau phay: ").split(',')
res = []
for b in lst:
if int(b, 2) % 5 == 0:
res.append(b)
print(','.join(res))
