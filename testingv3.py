def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string=input(m)
    return my_string


def review(F):
    for i in range(0, len(F)):
        output = "{} : {} ".format(F[i][0], F[i][1])
        print(output)


def fill_a_fruit_bowl(F):
    print("Please fill your bowl")
    run = True
    while run:
        type_fruit = get_string("What fruit do you want to add? -> ")
        quantity_fruit = get_integer("What quantity of fruit to add? -> ")
        temp_list = [type_fruit, quantity_fruit]
        F.append(temp_list)
        output = "You have added {} {}".format(quantity_fruit,type_fruit)
        print(output)
        more_fruit = get_string("CONTINUE TO ADD? (yes/no) -> ")
        if more_fruit == "no":
            print("You can now look at fruit list menu. Thank you.")
            run = False


def print_with_indexes(F):
    for i in range(0, len(F)):
        output = "{:5} ---- {:12}  ----- {:<10}".format(i, F[i][0], F[i][1])
        print(output)


def update_fruit(F):
    # test that the list has something in it
    if len(F) == 0:
        print("There is nothing in your fruit bowl")
        return None
    print_with_indexes(F)
    chosen_index = get_integer("Please chose the index number of the fruit you want to change: -> ")
    output = "You have chosen {} fruit".format(F[chosen_index][0])
    print(output)
    add_or_subtract = get_string("Would you like to add or subtract this fruit? -> ")
    if add_or_subtract == "add":
        adding = get_integer("How many of this fruit do you want to add? -> ")
        F[chosen_index][1] += adding
        output = "You have added {} {} to your {} total".format(adding, F[chosen_index][0], F[chosen_index][0])
        print(output)
        output = "You now have {} {}".format(F[chosen_index][1], F[chosen_index][0])
        print(output)
    if add_or_subtract == "subtract":
        subtract = get_integer("How many of this fruit do you want to subtract? -> ")
        F[chosen_index][1] -= subtract
        output = "You have subtracted {} {} from your {} total".format(subtract, F[chosen_index][0], F[chosen_index][0])
        print(output)
        output = "You now have {} {}".format(F[chosen_index][1], F[chosen_index][0])
        print(output)


def menu():
    #fruit_list = []

    fruit_list = [
        ["Orange", 2],
        ["Raspberries", 35],
        ["Apple", 5],
        ["Blueberries", 220]
    ]

    #fill_a_fruit_bowl(fruit_list)

    my_menu = '''
        U: Update
        R: Review
        Q: Quit
        '''

    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please enter choice: ->")
        print("." * 60)
        if choice == "U":
            update_fruit(fruit_list)
        elif choice == "R":
            review(fruit_list)
            print("." * 60)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")


if __name__ == "__main__":
    menu()
