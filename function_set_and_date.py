"""
This program allows you to get a set of words, the number of repetitions of words in the text,
converted dates from the text.
Before you start, you need to copy the text to the file 'mytext.txt'.
"""

from array_sets import get_array_sets
from stat_dict_text import get_stat_dict_text
from get_date import get_date_text


def set_words(w, result):
    """Getting set words"""

    if len(w) > 1:  # filtering words
        k = 0
        s = 1
        set_ = w[k]

        while len(set_) == 0:
            s += 1
            k += 1
            set_ = w[k]  # getting first set words
        while s < len(w):
            set_ = set.intersection(set_, w[s])  # getting set words from text
            s += 1
        if set_ == set():  # filtering results
            result.append('Not set')
        else:
            result.append('Set: ')
            result.append(set_)
    else:
        result.append('Error: Not Data')
    return result


if __name__ == "__main__":
    texts = open('mytext.txt')
    for text in texts:
        print('Text: ', text)

        if len(text) > 0:
            word_input = text.split('.')  # data input

            if len(word_input) > 0:  # filtering data input

                """Getting set words"""

                print('---------- Getting Set Of Words ----------')
                w = get_array_sets(word_input)  # getting array with sets words from text
                result = []
                res = set_words(w, result)
                if len(res) == 1:
                    print(res[0])
                else:
                    print(res[0])
                    print(res[1])

                """Getting number of word repetitions from text"""

                print('---------- Getting Number Of Words Repetitions From Text ----------')
                st_w = get_stat_dict_text(word_input)  # getting a dictionary
                if len(st_w) > 0:  # filtering results
                    print('Top words: ')
                    for i in st_w:
                        print(i, ':', st_w[i])
                else:
                    print('Error: Not Data')

                """Getting date from text"""

                print('---------- Getting Date From Text ----------')
                date = []
                get_date_text(word_input, date)  # getting date from text

                print('Date: ')
                if len(date) > 0:  # filtering results
                    for i in date:
                        print(i)
                else:
                    print('Not Date')
            else:
                print('Not Data')
        else:
            print('Not Data')
