people = {}

tech_id = int(input("what is your tech ID: "))
name = input("what is your name: ")

def add_to_dictionary(Name, Tech_ID):
    people[Name] = Tech_ID

person1 = add_to_dictionary(name,tech_id)


