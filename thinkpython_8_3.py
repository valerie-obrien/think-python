def string_back(string):
    index = -1
    while index < len(string):
        letter = string[index]
        print(letter)
        if index == -1 * len(string):
            break
        index = index - 1

string_back('ttub')