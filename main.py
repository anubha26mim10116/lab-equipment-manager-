equipment = []

while True:
    print("\n===== College Lab Equipment Manager =====")
    print("1. Add Equipment")
    print("2. View Equipment")
    print("3. Search Equipment")
    print("4. Delete Equipment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter equipment name: ")
        quantity = int(input("Enter quantity: "))

        equipment.append({
            "name": name,
            "quantity": quantity
        })

        print("Equipment added successfully!")

    elif choice == "2":
        if len(equipment) == 0:
            print("No equipment available.")
        else:
            print("\nAvailable Equipment:")
            for item in equipment:
                print("Name:", item["name"], "| Quantity:", item["quantity"])

    elif choice == "3":
        search = input("Enter equipment name to search: ")

        found = False

        for item in equipment:
            if item["name"].lower() == search.lower():
                print("Equipment found!")
                print("Name:", item["name"])
                print("Quantity:", item["quantity"])
                found = True

        if found == False:
            print("Equipment not found.")

    elif choice == "4":
        delete_name = input("Enter equipment name to delete: ")

        found = False

        for item in equipment:
            if item["name"].lower() == delete_name.lower():
                equipment.remove(item)
                print("Equipment deleted successfully!")
                found = True
                break

        if found == False:
            print("Equipment not found.")

    elif choice == "5":
        print("Thank you for using College Lab Equipment Manager!")
        break

    else:
        print("Invalid choice. Please try again.")