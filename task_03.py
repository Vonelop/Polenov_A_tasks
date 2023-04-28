def max_odd(array):
    max_odd_value = -1
    for value in array:
        if type(value) == int or type(value) == float:
           if value > max_odd_value and value % 2 == 1:
               max_odd_value = int(value)
    if max_odd_value == -1:
        return None
    return max_odd_value
