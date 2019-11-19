# palindrome

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    n = len(word)
    m = int(n / 2)
    if first(word) != last(word):
        return False
    elif n % 2 == 0 and word[1] == word[-2] and word[2] == word[-3]:
        return True
    elif n % 2 != 0 and word[m - 1] == word[m + 1] and word[m - 2] == word[m + 2]:
        return True

print(is_palindrome('civic'))        