def odd_even(para):
    largest_even = para[0]
    smallest_odd = para[0]
    for i in range(1, len(para)):
        if para[i] % 2 == 0:
            if largest_even < para[i]:
                largest_even = para[i]
        else:
            if smallest_odd > para[i]:
                smallest_odd = para[i]

    return largest_even - smallest_odd


# print(odd_even([1, 2, 4, 6]))


def prime_numbers(number):
    list_num = list()
    for i in range(number):
        if is_prime(i):
            list_num.append(i)
    return list_num


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


print(prime_numbers(8))
