def check_key_access(user_name):
    if user_name == "Kento":
        return True
    return False


if __name__ == "__main__":
    print(check_key_access("Kento"))
    print(check_key_access("Peter"))