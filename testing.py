def get_integer(m):
    my_integer=int(input(m))
    return my_integer


def get_string(m):
    my_string=input(m)
    return my_string


def review(L):
    for i in range(0, len(L)):
        output = "{} : {} ".format(L[i][0], L[i][1])
        print(output)

def menu():
    my_list =[
        ["Orange", "2"],
        ["Raspberries", "35"],
        ["Apple", "5"],
        ["Blueberries", "220"]
    ]
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
            review(my_list)
            print("." * 60)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")



# this is the start point
# this is the main function
# this programme will only run and kick off you you open this file
# name means the name file
if __name__ == "__main__":
    menu()
