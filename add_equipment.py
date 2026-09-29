def add_equipment(equipment):
    name = input("Enter equipment name: ")
    quantity = int(input("Enter quantity: "))

    equipment.append({
        "name": name,
        "quantity": quantity })

print("Equipment added successfully!")