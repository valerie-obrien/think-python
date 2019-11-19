# def print_n(s, n):
#    if n <= 0:
#        return
#    print(s)
#    print_n(s, n-1)

#print_n(5, 2)

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n(3, 2)