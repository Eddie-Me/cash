#Create a dictonary with items as keys and values as prices
item_name = {
    "apple": 1.25,
    "pear" : 1.00,
    "grapes": 0.25,
    "orange": 3.00
}

#Now inventory
inventory = {
    "apple": 2,
    "pear": 1,
    "grapes": 25,
    "orange": 3
}

shopping_car =[]
total =[]
#main menu with options
def main_menu():
    print("Welcome! What can I help you with today?")
    print("1.Buy something!")
    print("2.Display the inventory")
    print("3.Show my shopping car")
    print("4.Quit")
    print("Please, choose a number.")
    choice = input().lower()
    if choice == "1":
        buying()
    elif choice == "2":
        show_inventory()
    elif choice =="3":
        show_car()
    elif choice =="4":
        quit()
    else:
        print ("Invalid choice, try again.\n")
        main_menu()

def buying():
    print("Please, type the name of what you want to buy")
    to_buy =input().lower()
    if to_buy in inventory:
        print(check_vowel(to_buy.capitalize()),"right?\n(Type y/n)")
        answer= input().lower()
        if answer == "yes"or answer== "y":
            shopping_car.append(to_buy)
            print("Added to shopping car!\nGoing to the main menu.")
            main_menu()
        elif answer =="no" or "n":
            go_back =input("Do you want to coninue buying or go to your shopping car?(Type BUY or CAR)\n").lower()
            if "buy" in go_back:
                buying()
            elif "car" in go_back:
                show_car()
            else:
                print("Invalid option, please try again")
            return 
        else:
            print("Invalid option, please try again")
            buying()

def show_inventory():
    for key, value in item_name.items():
        print(f"{key.capitalize()}: ${value}\n")



def show_car():
    print("All the things you bought: ", shopping_car)
    for items in shopping_car:
        total.append(item_name[items])
    amount_to_pay = sum(total)
    print("$",amount_to_pay,"\n")
    

def check_vowel(to_buy):
    vowel='a'
    if to_buy[0].lower() in vowel:
        return f"So do you want an {to_buy},"
    else:
        return f"So do you want a {to_buy},"





while True:
    main_menu()