#my variables
inventory = []
running = True
#------------------------------------------------------------------------------------------------
#difficulty selection
def choose_difficulty():
    print("\n--- CHOOSE DIFFICULTY ---")
    print("1. Easy - 150 gold")
    print("2. Normal - 100 gold")
    print("3. Hard - 50 gold")

    difficulty = input("Choose your difficulty: ")

    match difficulty:
        case "1":
            print("You selected Easy!")
            return 150

        case "2":
            print("You selected Normal!")
            return 100

        case "3":
            print("You selected Hard!")
            return 50

        case _:
            print("Invalid choice! Normal difficulty selected.")
            return 100
#------------------------------------------------------------------------------------------------
#player gold starting amount based on difficulty
player_gold = choose_difficulty()
#------------------------------------------------------------------------------------------------
#menu
def show_menu():
    print("\n========== SHOP MENU ==========")
    print("Your gold:", player_gold)
    print("1. Buy Sword - 50 gold")
    print("2. Buy Shield - 40 gold")
    print("3. Buy Potion - 20 gold")
    print("4. Buy Bow - 60 gold")
    print("5. Show inventory")
    print("6. Sell item")
    print("7. Work (+20 gold)")
    print("8. Exit shop")
    print("===============================")
#------------------------------------------------------------------------------------------------
#inventory
def show_inventory(inventory):
    print("\n--- YOUR INVENTORY ---")

    if len(inventory) == 0:
        print("Your inventory is empty.")

    else:
        for item in inventory:
            print(item)
#------------------------------------------------------------------------------------------------
#broke or not
def can_buy(gold, price):

    if gold >= price:
        return True

    else:
        return False
#------------------------------------------------------------------------------------------------
#responsible for buying items
def buy_item(gold, inventory, item_name, price):

    if can_buy(gold, price):
        gold -= price
        inventory.append(item_name)

        print(f"You bought a {item_name}!")
        print("Remaining gold:", gold)

    else:
        print("Not enough gold!")

    return gold
#------------------------------------------------------------------------------------------------
#you selling your stuff
def sell_item(gold, inventory, item_name):

    if item_name in inventory:

        inventory.remove(item_name)

        if item_name == "Sword":
            gold += 25

        elif item_name == "Shield":
            gold += 20

        elif item_name == "Potion":
            gold += 10

        elif item_name == "Bow":
            gold += 30

        print(f"You sold your {item_name}!")
        print("Your new gold balance:", gold)

    else:
        print(f"You don't have a {item_name} to sell!")

    return gold
#------------------------------------------------------------------------------------------------
#finaly a job to earn some gold
def work(gold):

    gold += 20

    print("You worked and earned 20 gold!")
    print("Your new gold balance:", gold)

    return gold
#------------------------------------------------------------------------------------------------
#lets run the shop
while running:

    show_menu()

    choice = input("Choose an option: ")

    match choice:

        case "1":
            player_gold = buy_item(
                player_gold, inventory, "Sword", 50
            )

        case "2":
            player_gold = buy_item(
                player_gold, inventory, "Shield", 40
            )

        case "3":
            player_gold = buy_item(
                player_gold, inventory, "Potion", 20
            )

        case "4":
            player_gold = buy_item(
                player_gold, inventory, "Bow", 60
            )

        case "5":
            show_inventory(inventory)

        case "6":
            item_to_sell = input(
                "Enter the name of the item you want to sell: "
            )

            player_gold = sell_item(
                player_gold, inventory, item_to_sell
            )

        case "7":
            player_gold = work(player_gold)

        case "8":
            print("Thanks for visiting the Fantasy Shop!")
            running = False

        case _:
            print("Invalid choice! Please try again.")

        #somethings wrong with my commits
