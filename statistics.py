"""
This function records and returns the number of repetitions of words in the dictionary,
determines the maximum number of word repetitions.
"""


def get_statistics(set_w, total_words):
    w_dict = {}
    max_value = 0
    for i in set_w:
        count_words = 0
        for j in total_words:
            if j == i:
                count_words += 1
        w_dict[i] = count_words  # record in the dictionary the number of repetitions of words
        if count_words > max_value:
            max_value = count_words  # determining the maximum number of word repetitions
    value = max_value

    # definition of a minimum value
    if value >= 15:
        min_value = max_value - 10
    elif 15 < value > 9:
        min_value = max_value - 5
    elif 10 < value > 4:
        min_value = max_value - 3
    else:
        min_value = 0

    top_words = {}
    while value > min_value:
        for i in w_dict:
            if w_dict[i] == value:
                top_words[i] = value  # the creation of dictionary
        value -= 1
    return top_words
