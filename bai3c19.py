import math
P = []
for num in range(2, 10**6):
is_prime = True
for i in range(2, int(math.sqrt(num)) + 1):
if num % i == 0:
is_prime = False
break
if is_prime:
P.append(num)
P = tuple(P)
print(len(P))
