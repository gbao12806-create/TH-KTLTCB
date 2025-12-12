 p = 1000000
    rate = 0.06
    years = 3
    for _ in range(years):
        p += p*rate
    print("So tien sau 3 nam:", p)
