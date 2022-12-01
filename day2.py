def convert_add(list):
    # Normal way to convert
    # int_list = 0
    # for i in list:
    #     int_list += int(i)
    # return int_list

    # pythonic way
    return sum(map(int, list))


print(convert_add([1, 3, 5]))


def check_duplicates(list):
    hashmap = {}
    for i in list:
        if i in hashmap:
            return i
        else:
            hashmap[i] = 1


print(check_duplicates(["apple", "orange", "apple"]))
