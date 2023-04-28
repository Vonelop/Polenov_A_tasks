def connect_dicts(dict1, dict2):
    sum_value_1 = sum(dict1.values())
    sum_value_2 = sum(dict2.values())
    intermediate_dict = {}
    if len(dict1) > len(dict2):
        for key,value in dict1.items():
            if key in dict2:
                if sum_value_1 > sum_value_2:
                    if value >= 10:
                        intermediate_dict[key] = value
                        del dict2[key]
                else:
                    if value >= 10:
                        intermediate_dict[key] = dict2[key]
                        del dict2[key]
            else:
                if value >= 10:
                    intermediate_dict[key] = value
        if len(dict2) > 0:
            for key, value in dict2.items():
                if value >= 10:
                    intermediate_dict[key] = value
    else:
        for key,value in dict2.items():
            if key in dict1:
                if sum_value_2 >= sum_value_1:
                    if value >= 10:
                        intermediate_dict[key] = value
                        del dict1[key]
                else:
                    if value >= 10:
                        intermediate_dict[key] = dict1[key]
                        del dict1[key]
            else:
                if value >= 10:
                    intermediate_dict[key] = value
        if len(dict1) > 0:
            for key, value in dict1.items():
                if value >= 10:
                    intermediate_dict[key] = value
    finally_sort = sorted(intermediate_dict.items(), key = lambda  x: x[1])
    return dict(finally_sort)
