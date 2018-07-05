"""
This function takes the original text fragment, filters words and returns array of words set.
"""

import get_total_words
import statistics


def get_stat_dict_text(word_input):
    total_texts = []
    for i in word_input:  # word filter and getting words
        if len(i) > 0:
            i_m_ = i.split()
            for m in i_m_:
                i_ = m.split(',')[0]
                if len(i_) > 0:
                    total_texts.append(i_)  # writing words to an array

    totals_words_ = get_total_words.get_total_words(total_texts)  # getting array of words
    set_w = set(totals_words_)  # getting set of total_words
    stat = statistics.get_statistics(set_w, totals_words_)  # getting array of top words
    return stat
