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
    type_fruit = get_string("What fruit do you want to add? -> ")
    quantity_fruit = get_integer("What quantity of fruit to add? -> ")
    temp_list = [type_fruit, quantity_fruit]
    F.append(temp_list)
    output = "You have added {} {}".format(quantity_fruit,type_fruit)
    print(output)


def menu():
    fruit_list = []
    fill_a_fruit_bowl(fruit_list)

    my_menu = '''
        R: Review
        Q: Quit
        '''

    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please enter choice: ->")
        print("." * 60)
        if choice == "R":
            review(fruit_list)
            print("." * 60)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")


if __name__ == "__main__":
    menu()
