from add_equipment import add_equipment
from view_equipment import view_equipment
from search_equipment import search_equipment

equipment = []

while True:
    print("\n===== College Lab Equipment Manager =====")
    print("1. Add Equipment")
    print("2. View Equipment")
    print("3. Search Equipment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_equipment(equipment)

    elif choice == "2":
        view_equipment(equipment)

    elif choice == "3":
        search_equipment(equipment)

    elif choice == "4":
        print("Thank you for using College Lab Equipment Manager!")
        break

    else:
        print("Invalid choice. Please try again.")