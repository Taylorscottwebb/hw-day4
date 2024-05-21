cart = []

print("Lets go grocery shopping!")
while True:
    user_input = input("Tell us what you'd like to add  to your cart or say 'quit' to quit or 'remove' to remove item: ")
    if user_input == "quit":
        print("Thanks for shopping here are your items: ")
        for item in cart:
            print(item)
        break
    elif user_input == "remove":
        remove_item = input("what item do you want to remove? ")
        for item in cart:
            cart.remove(remove_item)
            print(remove_item, " is removed from the shopping cart.")

    else:
        cart.append(user_input)
        print(f"Your cart so far {cart}")


        
            