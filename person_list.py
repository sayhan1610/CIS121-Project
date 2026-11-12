# All the people known in a list.
people1 = ["Sayhan", "Marco", "Kento", "Matt"]

def check_people(people):
    if people in people1:
        return "known person"
    return "unknown person"


if __name__ == "__main__":
    user_data = input("Enter the first name of the resident: ")
    print(check_people(user_data))