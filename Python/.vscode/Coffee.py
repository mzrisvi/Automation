# Coffee Ordering App
def display_menu():
    """Displays the available coffee options and their prices."""
    print("*** Welcome to the Coffee Ordering App! ***")
    menu = {
        "espresso": 3.00,
        "latte": 4.50,
        "lappuccino": 4.00,
        "americano": 3.50
    }
    print("*** Our Menu ***")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ${price:.2f}")
    return menu

def take_order(menu):
    """Takes the user's order and calculates the total."""
    order = {}
    total_cost = 0.0

    while True:
        choice = input("What would you like to order? (type 'done' to finish): ").lower()
        if choice == 'done':
            break
        elif choice in menu:
            try:
                quantity = int(input(f"How many {choice}s would you like? "))
                if quantity > 0:
                    order[choice] = order.get(choice, 0) + quantity
                    total_cost += menu[choice] * quantity
                else:
                    print("Quantity must be a positive number.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Sorry, that's not on our menu. Please choose from the available options.")
    
    return order, total_cost

def main():
    """Main function to run the coffee ordering app."""
    menu = display_menu()
    user_order, final_cost = take_order(menu)

    if user_order:
        print("\n--- Your Order ---")
        for item, quantity in user_order.items():
            print(f"{item.capitalize()} x {quantity}")
        print(f"\nYour total is: ${final_cost:.2f}")
        print("Thank you for your order!")
    else:
        print("No order placed. Goodbye!")

if __name__ == "__main__":
    main()