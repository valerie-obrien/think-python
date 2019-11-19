def count(word, letter):
    ct = 0
    for i in word:
        if i == letter:
            ct = ct + 1
    print(ct)

count('banana', 'n')