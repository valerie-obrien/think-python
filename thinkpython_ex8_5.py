def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

# print(rotate_letter('a', 3))
    

def rotate_word(word, n):
    res = ''    
    for letter in word:
        res += rotate_letter(letter, n)
    return res

print(rotate_word('IBM', -3))
