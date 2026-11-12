from add_dictionary import find_person


def check_key_access(user_name):
    resident = find_person(user_name)
    return resident is not None and resident["key_access"]


if __name__ == "__main__":
    print(check_key_access("Kento"))
    print(check_key_access("Peter"))