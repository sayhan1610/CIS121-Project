name = input("what is your name?: ")
tech_id = int(input("what is your tech id?: "))

#function verifies the person's name and tech ID match
def find_person(people):
    title = ""
    count = 0
    for person in people:
        if name == person:
            if tech_id == people[person]:
                count = count + 1
                title = title + person
    if count == 1:
        return "correct"
    else:
        return "incorrect"





people1 = {"Marco":1234567892, "Sayhan":5674839203,"Kento":7864538902}

# two factor authentication basically with a random 4 digit number
import random
if find_person(people1) == "correct":
    value = random.randint(0,9999)
    print(value)
    number = int(input("enter 4 digit number:"))
    if value == number:
        print("verification complete")
    else:
        print("")
else:
    print("invalid name or tech ID")