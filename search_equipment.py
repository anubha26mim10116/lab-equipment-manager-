def search_equipment(equipment):
    search = input("Enter equipment name to search: ")

    found = False

    for item in equipment:
        if item["name"].lower() == search.lower():
            print("Equipment found!")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            found = True
            break

    if found == False:
        print("Equipment not found.")