print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

res = []
for num in range(1000, 3001):
if all(int(c) % 2 == 0 for c in str(num)):
res.append(str(num))
print(','.join(res))

