def print_twice(arg):
    print(arg)
    print(arg)

def do_twice(func, arg):
    func(arg)
    func(arg)

def print_spam():
    print('spam')

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')