import random

def walk(allItems, wizardInventory):
    unequippedItems = [item for item in allItems if item not in wizardInventory]
    randomItem = random.choice(unequippedItems)
    print(f"While walking down a path, you see a {randomItem}")
    grab = input("Do you want to grab it (y/n)")
    if grab.lower() == "y":
        if len(wizardInventory) >= 4:
            print("You can't carry any more items. Drop something first")
        else:
            wizardInventory.append(randomItem)
            print(f"You picked up a {randomItem}")
    else:
        print("Ok fine you didn't grab it")

def show(wizardInventory):
    for i, item in enumerate(wizardInventory, start=1):
        print(f"{i}. {item}")

def loadAllItems(allItems):
    with open("wizard_all_items.txt") as file:
        for item in file:
            item = item.replace("\n", "")
            allItems.append(item)

def loadInventory(wizardInventory):
    with open("inventory.txt") as file:
        for item in file:
            item = item.replace("\n", "")
            wizardInventory.append(item)

def saveInventory(wizardInventory):
    with open("inventory.txt", "w") as file:
        for item in wizardInventory:
            file.write(f"{item}\n")

def drop(wizardInventory):
    numberToDrop = int(input("Number: "))
    if numberToDrop > 0 and numberToDrop <= len(wizardInventory):
        removedItem = wizardInventory.pop(numberToDrop-1)
        print(f"You dropped a {removedItem}")
    else:
        print("Invalid number for item")

def printMenu():
    print("The Wizard Inventory program")
    print()
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop - Drop an item")
    print("exit - Exit program")

def main():
    allItems = []
    loadAllItems(allItems)
    wizardInventory = []
    loadInventory(wizardInventory)
    printMenu()
    while True:
        command = input("Command: ")
        if command.lower() == "walk":
            walk(allItems, wizardInventory)
        elif command.lower() == "show":
            show(wizardInventory)
        elif command.lower() == "drop":
            drop(wizardInventory)
        elif command.lower() == "exit":
            break
        else:
            print("invalid command, try again")
    print("Bye!")

if __name__ == "__main__":
    main()
