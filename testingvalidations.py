def validate_integer(m, min, max, minerror, maxerror):
    while True:
        try:
            quantity_fruit = int(input(m))
        except ValueError:
            print("unfortunately your entry is not valid. A whole number is needed")
            continue
        if quantity_fruit < min:
            print(minerror)
            continue
        elif quantity_fruit > max:
            print(maxerror)
            continue
        else:
            return quantity_fruit



if __name__ == "__main__":
    quantity_fruit = validate_integer("Please enter your number", 0, 20)
    print(quantity_fruit)