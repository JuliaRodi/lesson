def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if int(str_number[-1]) == 0:
        return get_multiplied_digits(int(str_number[0:-1]))
    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
