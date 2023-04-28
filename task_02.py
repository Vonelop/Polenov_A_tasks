def coincidence(*args):
    final_list = []
    if len(args) == 0:
        return final_list
    else:
        for i in range(len(args[0])):
            if type(args[0][i]) == int or type(args[0][i]) == float:
                if args[1].start <= args[0][i] < args[1].stop:
                    final_list.append(args[0][i])
    return final_list

