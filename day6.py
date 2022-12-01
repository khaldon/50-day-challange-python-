def user_name(email):
    return email.replace("@gmail.com", "")


# print(user_name("ben@gmail.com"))


def zeroed(input_list):
    input_list[0] = 0
    input_list[len(input_list) - 1] = 0
    return input_list


print(zeroed([2, 5, 7, 8, 9]))
