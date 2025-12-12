print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

s = input("Nhap cau: ")
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print("So chu cai la:", letters)
print("So chu so la:", digits)

