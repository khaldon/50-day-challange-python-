import math


def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)


print(divide_or_square(10))


def longest_value(data):
    return max(data.values(), key=len)


print(longest_value({"fruit": "apple", "color": "green"}))
