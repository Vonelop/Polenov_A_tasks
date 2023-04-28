def is_palindrome(string):
    string = str(string)
    new_string = ''
    for symbol in range(len(string)):
        if string[symbol] not in ", -!'?":
            new_string += string[symbol]
    new_string = new_string.lower()
    for i in range(len(new_string)//2):
        if new_string[i] != new_string[-1-i]:
            return False
    return True