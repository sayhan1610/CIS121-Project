from check_key_access import check_key_access
from loop import run_noise_detector
from person_list import check_people


def main():
    while True:
        print("\nRA Support System")
        print("1. Check noise level")
        print("2. Check resident")
        print("3. Check key access")
        print("q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            run_noise_detector()
        elif choice == "2":
            resident_name = input("Enter the first name of the resident: ").strip()
            print(check_people(resident_name))
        elif choice == "3":
            user_name = input("Enter the first name of the resident: ").strip()
            if check_key_access(user_name):
                print("Access granted.")
            else:
                print("Access denied.")
        elif choice == "q":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1, 2, 3, or q.")


if __name__ == "__main__":
    main()