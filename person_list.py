#All the people known in a list

people1 = ["Sayhan", "Marco", "Kento", "Matt"]

#checks if a person is in the known list

def check_people(people):
    if people in people1:
        return("known person")
    else:
        return ("unknown person")
    


user_data = input("Enter the first name of the resident: ")


print(check_people(user_data))