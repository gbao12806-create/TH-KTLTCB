print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

s = input("Nhập vào một chuỗi: ")
d = {}

for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print(d)

