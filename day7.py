def string_range(number):
    final_str = ""
    for i in range(number):
        final_str += str(i)
        if number - 1 == i:
            break
        else:
            final_str += "."

    return final_str


# print(string_range(6))


def dict_names(names):
    repeated_name = {}
    for i in range(len(names)):
        if names[i][0] == "S":
            if names[i] in repeated_name:
                repeated_name[names[i]] = repeated_name.get(names[i]) + 1
            else:
                repeated_name[names[i]] = 1

    return repeated_name


print(
    dict_names(
        names=[
            "Joseph",
            "Nathan",
            "Sasha",
            "Kelly",
            "Muhammad",
            "Jabulani",
            "Sera",
            "Patel",
            "Sera",
        ]
    )
)
