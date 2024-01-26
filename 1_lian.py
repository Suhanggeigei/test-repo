lucky=[5,6,9]
lucky.append(8)
print(lucky)


shopping_cart=["beer", "headphones"]
shopping_cart.remove('beer')
#移除已经完成，但是我们看不到结果，如需显示出，得打印。
shopping_cart[0]="wine"
print(shopping_cart)



names=["jack","wendy","lucy"]
greeting = "how are u? "
invite = "Dinner together!"

print(names[2] + "can\'t attend")
names[1] = "里昂"



#变量直接加号链接起来就好
print(greeting + invite + names[1])
print(greeting + invite + names[0])
print(greeting + invite + names[2])


print("Finding a bigger table ! ")
names.insert(0,"小胡")
names.insert(2,"小孙")
names.append("jordan")
print(greeting + invite + names[1])
print(greeting + invite + names[0])
print(greeting + invite + names[2])
print(greeting + invite + names[3])
print(greeting + invite + names[4])
print(greeting + invite + names[5])




def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Can't divide by zero"
    else:
        return num1 / num2
    
def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input()

    if choice == "1":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(add(num1, num2))

    
calculator()




def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


def calculator():
    print("Simple Calculator")
    print("=================")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please only use numbers.")
                continue

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            print(f"Result: {result}\n")

        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")


calculator()



# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    # 2. If it does, increase its quantity.
    # 3. If not, add the item to the inventory with the given quantity.
    pass

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    # 2. Print each item's name and its quantity.
    pass

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity.
    # 3. If the item doesn't exist, print a message indicating it's not found.
    pass

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        pass

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()










# Inventory Management System

# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.
    if item in inventory:
        # 2. If it does, increase its quantity.
        inventory[item] += quantity
    else:
        # 3. If not, add the item to the inventory with the given quantity.
        inventory[item] = quantity

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.
    for item, quantity in inventory.items():
        # 2. Print each item's name and its quantity.
        print(f"{item}: {quantity}")

# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    if item in inventory:
        # 2. If it does, update its quantity.
        inventory[item] = quantity
    else:
        # 3. If the item doesn't exist, print a message indicating it's not found.
        print(f"Error: Item '{item}' not found in inventory.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        # 2. If the choice is '2', call the view_inventory function.
        elif choice == "2":
            view_inventory()
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        elif choice == "3":
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        # 4. If the choice is '4', break the loop to exit the program.
        elif choice == "4":
            break
        # 5. For any other input, display an error message.
        else:
            print("Invalid choice. Please enter a valid choice.")

# Entry point of the program
if __name__ == "__main__":
    manage_inventory()






inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item}(s).")

def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"Updated {item} quantity to {quantity}.")
    else:
        print(f"{item} not found in inventory.")

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_item(item, quantity)
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")

manage_inventory()