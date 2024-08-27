import datetime

menu = {
    "Breakfast": {
        "1. Continental Breakfast": 8.99,
        "2. Indian Breakfast": 10.99,
        "3. Paneer Pakoda": 7.99,
        "4. Omelette": 9.99,
        "5. Chole Bhature": 8.99
    },
    "Lunch": {
        "1. Caesar Salad": 9.99,
        "2. Club Sandwich": 11.99,
        "3. Soup of the Day": 5.99,
        "4. Pizza": 12.99,
        "5. Burger Fries coke meal": 15.99
    },
    "Dinner": {
        "1. Steak Dinner": 24.99,
        "2. Pasta Primavera": 16.99,
        "3. Grilled Salmon": 19.99,
        "4. Vegetarian Platter": 14.99,
        "5. Paneer Tikka Masala": 18.99
    }
}

def show_menu(meal_time):
    print(f"\n{meal_time} Menu:")
    for item, price in menu[meal_time].items():
        print(f"{item}: ₹{price:.2f}")

def take_order(meal_time):
    show_menu(meal_time)
    order = []
    total = 0
    while True:
        item = input(f"Enter the item you want to order (or 'done' to finish): ")
        if meal_time == "Breakfast":
            if item == "1":
                item = "1. Continental Breakfast"
            elif item == "2":
                item = "2. Indian Breakfast"
            elif item == "3":
                item = "3. Paneer Pakoda"
            elif item == "4":
                item = "4. Omelette"
            elif item == "5":
                item = "5. Chole Bhature"
        elif meal_time == "Lunch":
            if item == "1":
                item = "1. Caesar Salad"
            elif item == "2":
                item = "2. Club Sandwich"
            elif item == "3":
                item = "3. Soup of the Day"
            elif item == "4":
                item = "4. Pizza"
            elif item == "5":
                item = "5. Burger Fries coke meal"
        elif meal_time == "Dinner":
            if item == "1":
                item = "1. Steak Dinner"
            elif item == "2":
                item = "2. Pasta Primavera"
            elif item == "3":
                item = "3. Grilled Salmon"
            elif item == "4":
                item = "4. Vegetarian Platter"
            elif item == "5":
                item = "5. Paneer Tikka Masala"
        if item.lower() == "done":
            break
        elif item in menu[meal_time]:
            order.append(item)
            price = menu[meal_time][item]
            total += price
            print(f"{item} has been added to your order. Current total: ₹{total:.2f}")
        else:
            print("Invalid item. Please try again.")
    return order, total

def calculate_gst(total):
    gst_rate = 0.18
    gst = total * gst_rate
    return round(gst, 2)

def print_bill(order, total, gst):
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 40)
    print(f"Good Food Restaurant - Bill")
    print(f"Date & Time: {current_time}")
    print(f"Name: {name}")
    print(f"Phone Number: {phone_number}")
    print("=" * 40)
    for item in order:
        print(f"- {item}")
    print("=" * 40)
    print(f"Subtotal: ₹{total:.2f}")
    print(f"GST (18%): ₹{gst:.2f}")
    print("=" * 40)
    print(f"Total: ₹{(total + gst):.2f}")
    print("=" * 40)
    print(f"Thank you {name} for dining with us!")

print("Welcome to the Good Food Restraurant Menu System!")
while True:
    meal_time = input("\n1. Breakfast \n2. Lunch  \n3. Dinner\nEnter the meal time or 'quit' to exit: ")
    if meal_time == "1":
        meal_time = "Breakfast"
    elif meal_time == "2":
        meal_time = "Lunch"
    elif meal_time == "3":
        meal_time = "Dinner"
    elif meal_time == "4":
        meal_time = "quit"
    if meal_time == "quit":
        break
    elif meal_time in menu:
        order, total = take_order(meal_time)
        if order:
            gst = calculate_gst(total)
            print_bill(order, total, gst)
    else:
        print("Invalid meal time. Please try again.")