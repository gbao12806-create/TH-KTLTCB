n = int(input("Nhap n: "))
pas = []
for i in range(n):
row = [1] * (i + 1)
for j in range(1, i):
row[j] = pas[i-1][j-1] + pas[i-1][j]
pas.append(row)
print(row)
