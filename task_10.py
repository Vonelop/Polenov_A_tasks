def count_words(string):
    finally_dict = {}
    trans_table = {ord('.'): None, ord('.'): None, ord(','): None, ord(':'): None, ord(';'): None, ord('!'): None, ord('?'): None, ord('-'): None}
    list_words = string.lower().split()
    new_list_words = []
    for word in list_words:
        new_word = word.translate(trans_table)
        if new_word != '':
            new_list_words.append(new_word)
    for word in new_list_words:
        if word not in finally_dict:
            finally_dict[word] = new_list_words.count(word)
    return finally_dict
    #понимаю, что это не оптимально, но пока другого решения не придумал


