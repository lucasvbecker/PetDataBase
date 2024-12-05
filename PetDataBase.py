class Pet:
    # name (str): The name of pet
    # age (int): The age of pet
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PetDatabase:
    # Adding, updating, removing, displaying, and searching pets
    def __init__(self):
        self.pets = []

    # Add pet
    def add_pet(self, name, age):
        self.pets.append(Pet(name, age))

    # Show pet
    def show_pets(self):
        if not self.pets:
            print("No pets in the database.")
            return

        # Header for table
        print(
            "+------------------------+\n| ID  | NAME      | AGE  |\n+------------------------+")

        # Display each pet in list
        for i, pet in enumerate(self.pets):
            print(f"| {i:3} | {pet.name:<9} | {pet.age:4} |")

        # Footer and total rows
        print(f"+------------------------+\n{len(self.pets)} rows in set.")
        


#MAIN FUNCTION
def main():
    db = PetDatabase()
    while True:

        # Display menu
        print("\nWhat would you like to do?")
        print("1) View all pets")
        print("2) Add more pets")
        print("7) Exit program\n")
        choice = input("Your choice: ")

        # View all pets
        if choice == "1":
            db.show_pets()

        # Add new pets
        elif choice == "2":
            print("\nEnter done to finish\n")
            while True:
                pet_info = input("add pet (name, age): ")
                if pet_info.lower() == "done":
                    break
                # Split and add pet
                name, age = pet_info.split()
                db.add_pet(name, int(age))
        # Exit the program
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            #INVALID CHOICE
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
