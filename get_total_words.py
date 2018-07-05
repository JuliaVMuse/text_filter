"""
This function allows you to clean and filter words and clear text.
The function writes the results to the array.
"""

import re


def get_total_words(text):
    total_words = []
    words = []
    for w in text:  # data cleaning and getting words
        if '«' in w and '»' not in w:
            words.append(w[1:len(w)].lower())
        elif '(' in w and ')' not in w:
            words.append(w[1:len(w)].lower())
        elif ')' in w and '(' not in w:
            words.append(w[0:len(w)-1].lower())
        elif '.»' in w and '«' not in w:
            words.append(w[0:len(w)-2].lower())
        elif '.)' in w and '(' not in w:
            words.append(w[0:len(w)-2].lower())
        elif '.' in w and '.»' not in w and '.)' not in w:
            words.append(w[0:len(w)-1].lower())
        elif ',' in w or '!' in w or ';' in w or ':' in w:
            words.append(w[0:len(w)-1].lower())
        else:
            words.append(w.lower())
    for word in words:  # word filter and clearing text
        stop_words = ['из-под', 'на', 'под', 'за', 'к', 'из', 'по', 'по', 'об', 'от', 'в', 'у', 'с', 'о',
                      'над', 'около', 'при', 'перед', 'даже', 'а', 'и', 'но', 'не', '—', '-', 'если',
                      'как', 'что', 'кто', 'это', 'то', 'будет', 'будут', 'всегда', 'можно', 'быть', '',
                      'the', 'in', 'так', 'же', 'км', 'чтобы', 'еще', 'ещё', 'я', 'когда',
                      'было', 'of', 'для', 'когда', 'сколько']
        if word not in stop_words:
            if '#' not in word and '-нибудь' not in word:
                pattern = r'[a-zA-Zа-яА-ЯёЁ]+'
                match = re.search(pattern, word)
                if match is not None:
                    m_w = match[0]
                    total_words.append(m_w)  # writing words to an array
    return total_words
