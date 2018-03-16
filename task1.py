def handle_numbers(number1, number2, number3):
    try:
        if type(number1) is int and type(number2) is int and type(number3) is int:
            if number1 % number3 == 0:
                return int(number2 // abs(number3) - number1 // abs(number3) + 1)
            return int(number2 // abs(number3) - number1 // abs(number3))
        else:
            return "Numbers must be int type"
    except ZeroDivisionError:
        return "number3 can not be 0"
