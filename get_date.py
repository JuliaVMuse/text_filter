"""
This function cleans the data, extracts, converts and writes dates to array.
The program returns array with converted dates.
"""

import re


def get_date_text(word_input, date):
    for i in word_input:
        s = i.split()

        for st in s:
            j = st.split(',')[0]
            patterns = [r'\d{2}-\d{2}-\d{4}', r'\d{2}/\d{2}/\d{4}']  # data cleaning and getting date
            for pattern in patterns:
                match = re.search(pattern, j)
                if match is not None:

                    day, month, year = '', '', ''
                    if len(match[0].split('-')) > 1:
                        day = match[0].split('-')[0]
                        month = match[0].split('-')[1]
                        year = match[0].split('-')[2]

                    elif len(match[0].split('/')) > 1:
                        day = match[0].split('/')[0]
                        month = match[0].split('/')[1]
                        year = match[0].split('/')[2]

                    months = {'01': 'january', '02': 'february', '03': 'march', '04': 'april', '05': 'may',
                              '06': 'june', '07': 'july', '08': 'august', '09': 'september', '10': 'october',
                              '11': 'november', '12': 'december'}

                    if day != '' and month != '' and year != '':  # date transformation
                        if month in months.keys():
                            new_date = day + ' ' + months[month] + ' ' + year
                            date.append(new_date)  # writing date to an array
    return date
