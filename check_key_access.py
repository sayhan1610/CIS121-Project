def check_key_access(user_name):
    if user_name == "Kento":
        return True
    else:
        return False

print(check_key_access("Kento"))
print(check_key_access("Peter"))