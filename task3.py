def handle_list_of_tuples(input_list):
    try:
        if type(input_list) is list:
            input_list.sort(key=lambda x: x[3], reverse=True)
            input_list.sort(key=lambda x: x[2], reverse=True)
            input_list.sort(key=lambda x: x[1], reverse=True)
            input_list.sort(key=lambda x: x[0])
        else:
            print("Input data must be a list of tuples")
    except IndexError:
        print("Inside list must be tuples with 4 values: name, age, height, weight")
