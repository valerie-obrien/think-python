fin = open('words.txt')
words = []
for line in fin:
    words.append(line.strip())

def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

def word_given_letters(words, letters):
    special_words = []
    for word in words:
        if uses_only(word, letters):
            special_words.append(word)
    return special_words

lst = word_given_letters(words, 'acefhlo')
for word in lst:
    print(word)