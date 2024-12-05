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
        print("+-------------------------+\n| ID  | NAME       | AGE  |\n+-------------------------+")
        # Display each pet in list
        for i, pet in enumerate(self.pets):
            print(f"| {i:3} | {pet.name:<10} | {pet.age:4} |")
        # Footer and total rows
        print(f"+-------------------------+\n{len(self.pets)} rows in set.")

    # Updates existing pet info
    def update_pet(self, pet_id, new_name, new_age):
        if 0 <= pet_id < len(self.pets):
            self.pets[pet_id].name = new_name
            self.pets[pet_id].age = new_age
        else:
            print("Invalid pet ID.")

    # Search pets by name
    def search_pet_by_name(self, name):
        matching_pets = [pet for pet in self.pets if pet.name.lower() == name.lower()]
        self.show_matching_pets(matching_pets)

    # Search pets by age
    def search_pet_by_age(self, age):
        matching_pets = [pet for pet in self.pets if pet.age == age]
        self.show_matching_pets(matching_pets)

    # Show matching pets
    def show_matching_pets(self, pets):
        if not pets:
            print("No matching pets found.")
            return
        
        # Header for table
        print("+------------------------+\n| ID  | NAME      | AGE  |\n+------------------------+")
        # Display matching pets
        for i, pet in enumerate(pets):
            print(f"| {i:3} | {pet.name:<9} | {pet.age:4} |")
        # Footer and total rows
        print(f"+------------------------+\n{len(pets)} rows in set.")

    # Remove pet
    def remove_pet(self, pet_id):
        if 0 <= pet_id < len(self.pets):
            removed_pet = self.pets.pop(pet_id)
            print(f"{removed_pet.name} is removed.")
        else:
            print("Invalid pet ID.")


#MAIN FUNCTION
def main():
    db = PetDatabase()
    while True:

        # Display menu
        print("\nWhat would you like to do?")
        print("1) View all pets")
        print("2) Add more pets")
        print("3) Update an existing pet")
        print("4) Remove an existing pet")
        print("5) Search pets by name")
        print("6) Search pets by age")
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

        # Update existing pet
        elif choice == "3":
            db.show_pets()
            pet_id = int(input("Enter the pet ID you want to update: "))
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            db.update_pet(pet_id, new_name, new_age)

        # Remove existing pet
        elif choice == "4":
            db.show_pets()
            pet_id = int(input("Enter the pet ID to remove: "))
            db.remove_pet(pet_id)

        # Search pets by name
        elif choice == "5":
            name = input("Enter a name to search: ")
            db.search_pet_by_name(name)

        # Search pets by age
        elif choice == "6":
            age = int(input("Enter age to search: "))
            db.search_pet_by_age(age)

        # Exit the program
        elif choice == "7":
            print("Goodbye!\n")
            break
        else:
            #INVALID CHOICE
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
