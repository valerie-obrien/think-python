def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

# print(has_no_e('wrong'))

fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)
print((count / 113809.0) * 100)