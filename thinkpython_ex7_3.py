import math

def estimate_pi():
    total = 0
    k = 0
    a = (2 * math.sqrt(2)) / 9801
    while True:
        b = (math.factorial(4 * k) * (1103 + 26390 * k))
        c = ((math.factorial(k)) ** 4) * 396 ** (4 * k)
        x = a * (b / c)
        total += x
        if x < 1e-15:
            break
        k += 1
    return 1 / total

print(estimate_pi())