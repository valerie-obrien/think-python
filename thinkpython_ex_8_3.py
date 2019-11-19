def is_palindrome(a):
    if a[::] == a[::-1]:
        return True
    else:
        return False

print(is_palindrome('cool'))