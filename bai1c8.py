print("sinh vien : Ho Gia Bao") 
print("ma so sv :245751030110059")
print("#############################")

a, b = 0, 1
total = 0
print("Dãy Fibonacci nhỏ hơn 4.000.000:")
print(a, end=" ")

while b < 4000000:
    print(b, end=" ")
    if b % 2 == 0:
        total += b
    a, b = b, a + b

print("\nTổng các số chẵn trong dãy Fibonacci là:", total)

