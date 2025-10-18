def MedievalMarket():
    itemlist = {
    "Sword" : 10.00, 
    "Shield" : 15.00,
    "Bow" : 30.00
    }

    player_inventory = {
        "Health Potion" : 50.00,
        "World Map" : 2.00
    }


    def PurchaseItem():
        while True:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
            print("                     ==Purchase Item==")
            print("")
            for item, price in itemlist.items():
                print(f"                      {item} = RM{price:.2f}")
            print("")
            print("0) Return")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("                What do you want to purchase?")
            ItemBuy = input("Type your desired item or return (0) : ")

            PurchaseChoice = str(ItemBuy)
            try:
                if PurchaseChoice in itemlist:
                    player_inventory[PurchaseChoice] = itemlist[PurchaseChoice]
                    del itemlist[PurchaseChoice]
                    print("     Item added to inventory and removed from shop!")
                    input("Press Enter to Countinue...")
                elif PurchaseChoice == '0':
                    return
                else:
                    print("Item not found!")
                    input("Press Enter to Countinue...")
            except:
                print("Wrong input!")

    def SellItem():
        while True:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
            print("                        ==Sell Item==")
            print("")
            for item, price in player_inventory.items():
                print(f"                      {item} = RM{price:.2f}")
            print("")
            print("0) Return")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("                  What do you want to sell?")
            ItemSell = input("Type item to sell or return (0) : ")

            SellChoice = str(ItemSell)
            try:
                if SellChoice in player_inventory:
                    itemlist[SellChoice] = player_inventory[SellChoice]
                    del player_inventory[SellChoice]
                    print("     Item has been removed from inventory!")
                    input("Press Enter to Countinue...")
                elif SellChoice == '0':
                    return
                else:
                    print("Item not found!")
                    input("Press Enter to Countinue...")
            except:
                print("Wrong input!")

    def PlayerInventory():
        while True:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
            for item, price in player_inventory.items():
                print(f"                      {item} = RM{price:.2f}")
            print("")
            print("0) Return")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            InventoryChoice = int(input("return? (0) : "))
            try:
                if InventoryChoice == 0:
                    return
                else:
                    print("Wrong Input!")
                    input("Press Enter to Countinue...")
            except:
                print("Wrong input!")
                return

    while True:
        print("==========================================================")
        print("")
        print("               ==Welcome to Medieval Market==")
        print("")
        print("                 1. Purchase Item")
        print("                 2. Sell Item")
        print("                 3. Player Inventory")
        print("                 4. Back")
        print("")
        print("==========================================================")

        user_input = (input("                 Enter number to navigate : "))

        try:
            choice = int(user_input)
            if choice == 1:
                PurchaseItem()
            elif choice == 2:
                SellItem()
            elif choice == 3:
                PlayerInventory()
            elif choice == 4:
                break
        except:
            print("Wrong Input!!")
            input("Press Enter to Countinue...")
