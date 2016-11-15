
dictionary_of_lists = {}

def main():
    print"Welcome! \n Let's do some shopping!! \nThis program allows you to create various lists. \n\nPlease choose from the following options: "
    menu()

def create_list(new_list):
    if new_list in dictionary_of_lists.keys():
        print "oops!  that list already exists."
        duplicate_list_choice = raw_input("would you like to: \nA. Dive into this list \nB. Try again to make a new list \nC. Go to main menu").lower()
        if duplicate_list_choice == "a":
            dive_list(new_list)
        elif duplicate_list_choice == "b":
            try_new_list = raw_input("What is the name of the shopping list you want to make?").lower()
            create_list(try_new_list)
        else:
            menu()
    else:
        dictionary_of_lists[new_list] = []
        print "OK - now you have a list called " + new_list + "." 
        while(True):
            user_new_list_choice = raw_input("Would you like to: \nA. add an item to this list or \nB. go back to main menu?")
            if user_new_list_choice.lower() == "a": 
                new_item = raw_input("OK - what do you want to add to this list?\nYou can add multiple items by separating each with a space and comma.").lower()
                add_to_list(new_list, new_items)
            else:
                menu()
    return True     #will this get me bakc to the menu whiel loop?

def dive_list(current_list):
    print "Ok, let's take a look at " + current_list
    while(True):
        dive_user_choice = raw_input("would you like to: \nA. See all the items in this list so far \nB. Add a new item \nC. Go back to main menu").lower()
        if dive_user_choice == "a":
            print dictionary_of_lists[current_list]
        elif dive_user_choice == "b":
            new_item = raw_input("OK - what do you want to add to this list?\nYou can add multiple items by separating each with a space and comma.").lower()
            add_to_list(current_list, new_items)
        else:
            menu()


def add_to_list(list_key, items):
    list_items = items.split(", ")
    for item in list_items:
        if item in dictionary_of_lists[list_key]:
            del list_items[list_key]
        elif item == "":
            del list_items{list_key]
        else:
            pass
    dictionary_of_lists[list_key] = dictionary_of_lists[list_key] + list_items



    if item in dictionary_of_lists[list_key]: 
        print "oops - already got that one!"

    this_list = dictionary_of_lists[list_key]
    this_list.append(item)
    return True

def menu():
    while(True):
        # print"To show the main menu, press 0."
        print"1 -- start a brand new list (and add items!)"
        print"2 -- see all my lists by name"
        print"3 -- dive into a specific list (more options!)"
        # print"To add an item to a shopping list, press 4."
        # print"To remove an item from a shopping list, press 5." 
        print"6 -- delete an entire list"
        print"7 -- exit this program"
        user_choice = int(raw_input("choose an option: "))
       
        if user_choice ==7:
            print "thanks for shopping!!"
            break
        elif user_choice == 0:
            pass
        elif user_choice == 1:
            new_list=raw_input("what is the name of the shopping list you want to make?").lower()
            create_list(new_list)
        elif user_choice == 2:
            print dictionary_of_lists
        elif user_choice == 3:
            list_key = raw_input("what list would you like to see? ")
            dive_list(list_key)
        elif user_choice == 4:
            # which_list = raw_input("what list would you like to add items to?")
            # which_item = raw_input("what item would you like to add?")
            # add_to_list(which_list, which_item)
            pass
        elif user_choice == 5:
            pass
        elif user_choice == 6:
            pass
        else:
            print "You did not select one of the provided options. Please select a number from 1-7. "



# if __name__ == '__main__':
main()