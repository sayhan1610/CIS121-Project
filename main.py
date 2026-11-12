from add_dictionary import add_to_dictionary
from check_key_access import check_key_access
from loop import run_noise_detector
from person_list import check_people


def main():
    while True:
        print("\nRA Support System")
        print("1. Check noise level")
        print("2. Check resident")
        print("3. Check key access")
        print("4. Add or update resident")
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
        elif choice == "4":
            resident_name = input("Enter the resident's name: ").strip()
            tech_id_text = input("Enter the resident's tech ID: ").strip()
            try:
                tech_id = int(tech_id_text)
                add_to_dictionary(resident_name, tech_id)
            except ValueError as error:
                print(error)
            else:
                print("Resident added or updated.")
        elif choice == "q":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1, 2, 3, 4, or q.")


if __name__ == "__main__":
    main()