def my_discount():
    price, discount = int(input()), int(input())
    discount = discount / 100
    return price - (price * discount)


# print(my_discount())


def tuple_student_sex(students):
    male_count = 0
    female_count = 0
    for gender in students:
        if gender == "female" or gender == "Female":
            female_count += 1
        elif gender == "male" or gender == "Male":
            male_count += 1
    return [("male", male_count), ("female", female_count)]


print(
    tuple_student_sex(
        students=[
            "Male",
            "Female",
            "female",
            "male",
            "male",
            "male",
            "female",
            "male",
            "Female",
            "Male",
            "Female",
            "Male",
            "female",
        ]
    )
)
