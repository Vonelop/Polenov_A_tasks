def multiply_numbers(inputs = None):
    new_inputs = str(inputs)
    if any([symbol.isdigit() for symbol in new_inputs]):
        finally_sum = 1
        for symbol in new_inputs:
            if symbol in '1234567890':
                finally_sum *= int(symbol)
        return finally_sum