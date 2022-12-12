def biggest_odd(string):
    biggest_number = 0
    a = [
        biggest_number := int(i)
        for i in string
        if int(i) % 2 != 0
        if biggest_number < int(i)
    ]

    return biggest_number


# print(biggest_odd("23569"))


def zeros_last(number):
    for i in range(len(number)):
        if 0 in number:
            if number[i] == 0:
                number.append(number.pop(i))
        else:
            return sorted(number)
    return number


def test_functions():
    assert zeros_last([1, 4, 6, 0, 7, 0, 9]) == [1, 4, 6, 7, 9, 0, 0]
    assert zeros_last([2, 1, 4, 7, 6]) == [1, 2, 4, 6, 7]


if __name__ == "__main__":
    test_functions()
    print("Everything passed")
