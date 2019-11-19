import math

def check_fermat(a, b, c, n):
    if n > 2 and a^n + b^n == c^n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

# check_fermat(a, b, c, n)


def user_fermat():
    '''Define variables based on user input
    '''
    a = int(float(input("Type a value for a: ")))
    b = int(float(input("Type a value for b: ")))
    c = int(float(input("Type a value for c: ")))
    n = int(float(input("Type a value for n: ")))
    check_fermat(a, b, c, n)

user_fermat()