def combine_anagrams(words_array):
    finally_group = []
    i = 0
    y = i + 1
    while i < len(words_array):
        intermediate_group = [words_array[i]]
        while y < len(words_array):
            first_word = sorted(list(words_array[i]))
            last_word = sorted(list(words_array[y]))
            if words_array[i] != words_array[y] and first_word == last_word:
                intermediate_group.append(words_array[y])
                del words_array[y]
            else:
                y += 1
        i += 1
        y = i + 1
        finally_group.append(intermediate_group)
    return finally_group