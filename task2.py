def handle_string(value):
    try:
        letters = 0
        digits = 0
        for symbol in value:
            if symbol.isdigit():
                digits += 1
            if symbol.isalpha():
                letters += 1
        print("Letters - {} \nDigits - {} \n".format(letters, digits))
    except TypeError:
        print("value must be string")

