def register_check(register):
    at_school = 0
    for i in register:
        if register[i] == "yes":
            at_school += 1
    return at_school


# print(
#     register_check(
#         register={"Michael": "yes", "John": "no", "Peter": "yes", "Mary": "yes"}
#     )
# )


def lower_case(names):
    store_lower_case = ()
    for i in names:
        if i.islower():
            store_lower_case = store_lower_case + (i,)
    return store_lower_case


print(lower_case(names=["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]))
