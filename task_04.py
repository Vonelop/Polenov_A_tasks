def sort_list(list):
    if len(list) == 0:
        return []
    else:
        min_value = min(list)
        max_value = max(list)
        for i in range(len(list)):
            if list[i] == max_value:
                list[i] = min_value
            elif list[i] == min_value:
                list[i] = max_value
        return list + [min_value]
