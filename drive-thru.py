def main():
    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)


def welcome():
    menu= ["Cheeseburger", "Fries", "Soda", "Ice cream", "Cookie"]
    print("Welcome to the restaurant!")
    print("Here the menu:")
    for food in range(len(menu)):
        print(f"{i+1}. {menu[i]}")


def get_item(order):
    if order == 1:
        print(")



if __name__ == "__main__":
    main()
