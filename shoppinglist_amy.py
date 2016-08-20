shoplist = {"main":["eggs","cheese"]}

def show_specific_list(name_list):
    return shoplist[name_list]

def add_list(shoplist):
    name_list = raw_input("Which list would you like to add? ").lower()
    shoplist[name_list] = []
    print "New list added:", name_list

def add_item(shoplist):
    print "Current lists are:", shoplist.keys()
    name_list = raw_input("Which list would you like to add to? ").lower()
    name_item = raw_input("Which item would you like to add? ").lower()
    if name_item in shoplist[name_list]:
        print "This item is already in the list."
    else:
        shoplist[name_list] = name_item
        print "Added to " + name_list + ": " + name_item

def remove_item(shoplist):
    print "Current lists are:", shoplist.keys()
    name_list = raw_input("Which list would you like to remove from? ").lower()
    print "Current items are:", shoplist[name_list]
    name_item = raw_input("Which item would you like to remove? ").lower()
    name_item_for_print = name_item
    if name_item not in shoplist[name_list]:
        print "This item is not in the list."
    else:
        shoplist[name_list].remove(name_item)
        print "Removed from " + name_list + ": " + name_item

def remove_list(shoplist):
    name_list = raw_input("Which list would you like to remove? ").lower()
    del shoplist[name_list]

def write_list_to_file(list_name):
    file_name = "Shopping_List.txt"
    with open(file_name, mode = "w") as my_file:
        for i in shoplist[list_name]:
            my_file.write(i)
            my_file.write('\n')

def menu():
    while True:
        print ""
        print "Select a Menu Option:"
        print "     1 - Show All Lists"
        print "     2 - Show Specific List"
        print "     3 - Add New List"
        print "     4 - Add Item"
        print "     5 - Remove Item"
        print "     6 - Remove List"
        print "     7 - Write List to File"
        print "     8 - Quit"
        choice = raw_input("-->  ")
        if choice not in str(range(8)):
            print "'" + str(choice) + "' was not a menu item."
        else:
            return int(choice)

def main():
    choice = None
    while choice != 8:
        choice = menu()
        if choice == 1:
            print shoplist
        elif choice == 2:
            print "Current lists are:", shoplist.keys()
            name_list = raw_input("Which list would you like to view? ").lower()
            print show_specific_list(name_list)
        elif choice == 3:
            add_list(shoplist)
        elif choice == 4:
            add_item(shoplist)
        elif choice == 5:
            remove_item(shoplist)
        elif choice == 6:
            remove_item(shoplist)
        elif choice == 7:
            print "Current lists are:", shoplist.keys()
            list_name = raw_input("Which list would you like to write to a file?")
            write_list_to_file(list_name)
        else:
            print "Goodbye."

if __name__ == '__main__':
    main()