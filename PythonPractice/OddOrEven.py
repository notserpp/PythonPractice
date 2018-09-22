def odd_or_even():
    while 1:
        number = int(raw_input("Enter a number(-1 to exit): "))
        if number == -1:
            break
        number_two= int(raw_input("Enter a second number: "))

        if number % 2 == 0:
            print number, "is an even number"
        if number_two % 2 == 0:
            print number_two, "is an even number"
        if number % 4 == 0:
            print number, "is a multiple of four"
        if number_two % 4 == 0:
            print number_two, "is a multiple of four"
        if number % number_two == 0:
            print number, "is evenly divisible by", number_two
        else:
            print number, "is an odd number"


odd_or_even()
