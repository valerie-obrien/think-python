import math

def mysqrt(a):    
    x = a
    while True:
        y = (x + a/x) / 2
        epsilon = 0.0000001
        if abs(y-x) < epsilon:
            break
        x = y
    return x

print(mysqrt(-2))


def test_square_root():
    c1 = 'a'
    c2 = 'mysqrt(a)'
    c3 = 'math.sqrt(a)'
    c4 = 'diff'
    h1 = c1 + '\t' + c2 + '\t' + c3 + '\t' + c4
    h2 = '-' * len(c1) + '\t' + '-' * len(c2) + '\t' + '-' * len(c3) + '\t' + '-' * len(c4)
    print(h1 + '\n' + h2)
    for a in range(1,10):
        print(f'{a}\t{mysqrt(a):.6f}\t{math.sqrt(a):.6f}\t{mysqrt(a) - math.sqrt(a):.6e}')

#test_square_root()