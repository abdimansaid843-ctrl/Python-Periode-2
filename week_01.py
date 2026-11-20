
# Player info
player_name = input("What is your name? ")
player_gold = 100
inventory = []

# winkel items
items = ["Sword", "Shield", "Potion", "Bow"]

# Main winkel menu
while True:
    print("\n=== Fantasy Item Winkel ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Winkel")
    print("7. Sell Item")
    print("8. View Gold")

    choice = input(f"welcome {player_name}! you have {player_gold} gold. What would you like to do? ")

    match choice:
        # Select item to buy
        case "1":
            item_name = "Sword"
            item_price = 50
            unique_item = True

        case "2":
            item_name = "Shield"
            item_price = 40
            unique_item = True

        case "3":
            item_name = "Potion"
            item_price = 20
            unique_item = False

        case "4":
            item_name = "Bow"
            item_price = 60
            unique_item = True

        # View inventory
        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print(item)
            continue

        # Exit winkel
        case "6":
            print("Thanks for visiting the Fantasy Item Winkel!")
            print("You have", player_gold, "gold left.")
            print("Goodbye!")
            break

        # Sell items
        case "7":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print(item)

                item_to_sell = input("Which item do you want to sell? ").title()

                match item_to_sell:
                    case "Sword":
                        sell_price = 25
                    case "Shield":
                        sell_price = 20
                    case "Potion":
                        sell_price = 10
                    case "Bow":
                        sell_price = 30
                    case _:
                        sell_price = 0

                if item_to_sell in inventory:
                    inventory.remove(item_to_sell)
                    player_gold += sell_price
                    print("You sold", item_to_sell, "for", sell_price, "gold!")
                    print("You now have", player_gold, "gold.")
                else:
                    print("You don't have that item!")

            continue

        case "8":
            print("You have", player_gold, "gold.")

        # Invalid menu option
        case _:
            print("Invalid choice! Please choose 1-8.")
            continue

    # Ask how many items the player wants
    amount = int(input("How many would you like to buy? "))

    # Check quantity
    if amount <= 0:
        print("Please enter a valid amount!")

    # Check unique items
    elif unique_item and item_name in inventory:
        print("You already own this item!")

    elif unique_item and amount > 1:
        print("You can only own one", item_name + "!")

    else:
        # Calculate total price
        total_price = item_price * amount

        # Check player's gold
        if player_gold >= total_price:
            player_gold -= total_price

            for i in range(amount):
                inventory.append(item_name)

            print("You bought", amount, item_name + "(s)!")
            print("You have", player_gold, "gold left.")

        else:
            print("Not enough gold!")
            print("You need", total_price, "gold.")
            print("You only have", player_gold, "gold.")
