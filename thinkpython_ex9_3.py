def avoids(word, letters):
    for char in word:
        if char in letters:
            return False
    return True
            

# print(avoids('hello', 'abce'))

letters = input("Type a list of forbidden letters: ")
fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, letters):
        count += 1
        print(word)