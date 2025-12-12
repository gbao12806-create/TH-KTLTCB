print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))

