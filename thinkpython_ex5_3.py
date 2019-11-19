import math

def is_triangle(a, b, c):
    if a > b + c:
        print('No')
    else:
        print('Yes')

# is_triangle(5, 2, 4)

def user_triangle():
    a = int(float(input('Length of side a: ')))
    b = int(float(input('Length of side b: ')))
    c = int(float(input('Length of side c: ')))
    is_triangle(a, b, c)

user_triangle()