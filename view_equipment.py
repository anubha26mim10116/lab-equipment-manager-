def view_equipment(equipment):
    if len(equipment) == 0:
        print("No equipment available.")
    else:
        print("\nAvailable Equipment:")

        for item in equipment:
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("--------------------")