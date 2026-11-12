from add_dictionary import find_person


def check_people(name):
    if find_person(name) is not None:
        return "known person"
    return "unknown person"


if __name__ == "__main__":
    resident_name = input("Enter the first name of the resident: ").strip()
    print(check_people(resident_name))
