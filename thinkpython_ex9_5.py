# Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
# and that returns True if the word uses all the required letters at least once. How many words are
# there that use all the vowels aeiou? How about aeiouy?

def uses_all(word, letters):
    return_value = True
    for char in letters:
        if char not in word:
            return_value = False
    return return_value


print(uses_all('hello', 'elhop'))