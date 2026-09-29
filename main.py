equipment = []


def add_equipment():
    name = input("Enter equipment name: ")
    quantity = int(input("Enter quantity: "))

    equipment.append({
        "name": name,
        "quantity": quantity
    })

    print("Equipment added successfully!")


def view_equipment():
    if len(equipment) == 0:
        print("No equipment available.")
    else:
        print("\n===== Equipment List =====")

        for item in equipment:
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("-------------------------")


def search_equipment():
    name = input("Enter equipment name to search: ")

    for item in equipment:
        if item["name"].lower() == name.lower():
            print("\nEquipment found!")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            return

    print("Equipment not found.")


while True:
    print("\n===== College Lab Equipment Manager =====")
    print("1. Add Equipment")
    print("2. View Equipment")
    print("3. Search Equipment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_equipment()

    elif choice == "2":
        view_equipment()

    elif choice == "3":
        search_equipment()

    elif choice == "4":
        print("Thank you for using College Lab Equipment Manager!")
        break

    else:
        print("Invalid choice. Please try again.")