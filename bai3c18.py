print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

n = int(input("Nhap n: "))
fib = [0, 1]
while fib[-1] + fib[-2] < n:
fib.append(fib[-1] + fib[-2])
print(fib)

