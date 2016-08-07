shoplist = []

def add_item(shoplist):
    item = raw_input("Which item would you like to add? ").lower()
    if item in shoplist:
        print "This item is already in the list."
    else:
        shoplist.append(item)
        print "Added to list:", item

def remove_item(shoplist):
    item = raw_input("Which item would you like to remove? ").lower()
    if item not in shoplist:
        print "This item is not in the list."
    else:
        shoplist.remove(item)
        print "Removed from list:", item

def menu():
    while True:
        print ""
        print "Select a Menu Option:"
        print "     1 - Show Current List"
        print "     2 - Add Item"
        print "     3 - Remove Item"
        print "     4 - Quit"
        choice = raw_input("-->  ")
        if choice not in ["1","2","3","4"]:
            print "'" + str(choice) + "' was not a menu item."
        else:
            return int(choice)

def main():
    choice = None
    while choice != 4:
        choice = menu()
        if choice == 1:
            print shoplist
        elif choice == 2:
            add_item(shoplist)
        elif choice == 3:
            remove_item(shoplist)
        else:
            print "Goodbye."

if __name__ == '__main__':
    main()