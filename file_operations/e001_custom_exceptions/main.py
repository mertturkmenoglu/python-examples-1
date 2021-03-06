# Custom Exceptions
# Put Exceptions in a different file


class Error(Exception):
    """ Base class for our operations """
    pass


class TooBig(Error):
    """When the input is too big"""
    pass


class TooSmall(Error):
    """When the input is too small"""
    pass


real_number = 14
flag = 0
while flag == 0:
    try:
        number = int(input("Please enter the number: "))
        if number > real_number:
            raise TooBig
        elif number < real_number:
            raise TooSmall
        else:
            flag = 1
    except TooBig:
        print("Your number is bigger try again")
        print()
    except TooSmall:
        print("Your number is too small try again")
        print()
    else:
        print("You got it")
