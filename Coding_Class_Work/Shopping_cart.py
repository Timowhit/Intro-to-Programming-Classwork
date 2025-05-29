#menu
menu_selection = 0
prices = []
shopping_list = []

while(menu_selection != 5):

    print("1. Add item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute total")
    print("5. Quit")

    menu_selection = int(input("Please Enter an Action: "))

#out of bounds
    if menu_selection < 1 or menu_selection > 5:
        print("Invalid Entry")
        print()

#add
    if menu_selection == 1:
        item = input("What Item Would you Like to add? ")
        shopping_list.append(item)
        #price add
        price = float(input(f"What is the price of {item}?"))
        prices.append(price)
        print(f"{item} has been added to the cart")
        print()
        print()

#display list
    elif menu_selection == 2:
        print("Your Cart: ")
        for i in range(len(shopping_list[i])):
            print(f"{i+1}. {shopping_list[i]} - ${prices[i]}")
        print()
        print()

#remove item
    elif menu_selection == 3:
        item = int(input("What item would you like to remove? "))
        item -= 1

        if item < 0 or item > len(prices):
            print("Invalid selection. Item not in list")

        else:
            thing = shopping_list[item]
            shopping_list.pop(item)
            prices.pop(item)

            print(f"{thing} has been removed from the cart")

#total price
    elif menu_selection == 4:

        sum = 0
        for price in prices:
            sum += price
        
        print()
        print(f"The total is ${sum:.2f}")
        print()
        print()