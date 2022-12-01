def only_floats(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return 2
    else:
        return 1


# print(only_floats(12.1, 23))


def word_index(word):
    max_str = ""
    count = 1
    x = 0
    for i in range(1, len(word)):
        if word[x] > word[i]:
            max_str = word[x]
        elif word[x] < word[i]:
            max_str = word[i]
        elif word[x] == word[i]:
            count += 1

    if count == len(word):
        return 0
    else:
        return max_str


print(word_index(["vengeance", "vengeance"]))
