"""
This function takes text, filters words and writes set of words to array.
The program returns array with words sets.
"""

import get_total_words


def get_array_sets(word_input):
    word_arr = []

    for s in word_input:  # word filter and getting words
        if len(s) > 0:
            array_text = []
            sub = s.split()

            for m in sub:
                word = m.split(',')[0]
                if len(word) > 0:
                    array_text.append(word)  # writing words to an array

            total_words_ = get_total_words.get_total_words(array_text)  # getting array of words

            set_w = set(total_words_)  # getting set of total_words

            if len(set_w) > 0:  # set filter
                word_arr.append(set_w)  # writing words set to an array

    return word_arr
