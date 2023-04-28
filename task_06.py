class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(value):
    if len(value) > 2:
        raise WrongNumberOfPlayersError
    elif value[0][1] not in 'RPS' or value[1][1] not in 'RPS':
        raise NoSuchStrategyError
    else:
        if value[0][1] == 'P':
            if value[1][1] == 'P':
                return f'{value[0][0]} P'
            elif value[1][1] == 'S':
                return f'{value[1][0]} S'
            else:
                return f'{value[0][0]} P'
        elif value[0][1] == 'S':
            if value[1][1] == 'P':
                return f'{value[0][0]} S'
            elif value[1][1] == 'S':
                return f'{value[0][0]} S'
            else:
                return f'{value[1][0]} R'
        else:
            if value[1][1] == 'P':
                return f'{value[1][0]} P'
            elif value[1][1] == 'S':
                return f'{value[0][0]} R'
            else:
                return f'{value[0][0]} R'
