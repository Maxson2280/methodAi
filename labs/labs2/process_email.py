import numpy as np
from porterStemmer import porterStemmer
import re


def get_dictionary():
    with open('dictionary.txt') as f:
        dictionary = []
        for line in f:
            idx, w = line.split()
            dictionary.append(w)
    return np.array(dictionary)


def process_email(email):
    vocabList = get_dictionary()
    word_indices = []

    # приведение текста к нижнему регистру
    email = email.lower()

    # удаление html-тегов из текста письма
    rx = re.compile('<[^<>]+>|\n')
    email = rx.sub(' ', email)

    # числа заменяются на строку 'number'
    rx = re.compile('[0-9]+')
    email = rx.sub('number ', email)

    # ссылки заменяются на строку 'httpaddr'
    rx = re.compile('(http|https)://[^\s]*')
    email = rx.sub('httpaddr ', email)

    # электронные адреса заменяются на строку 'emailaddr'
    rx = re.compile('[^\s]+@[^\s]+')
    email = rx.sub('emailaddr ', email)

    # значок $ заменяется на строку 'dollar'
    rx = re.compile('[$]+')
    email = rx.sub('dollar ', email)

    # удаление не буквенно-цифровых символов
    rx = re.compile('[^a-zA-Z0-9]')
    email = rx.sub(' ', email).split()

    for str in email:
        # приведение каждого слова к существительному в единственном числе
        try:
            str = porterStemmer(str.strip())
        except:
            str = ''
            continue

        if len(str) < 1:
            continue

        # TODO: необходимо в word_indices добавить индекс слова str из словаря vocabList.
        ans = np.where(np.array(vocabList) == str)
        if len(ans[0]) > 0:
            word_indices.append(ans[0][0])

    return word_indices


def email_features(word_indices):
    n = 1899  # общее число слов в словаре
    x = np.zeros(n)

    # TODO: необходимо установить в 1 элементы массива x,
    for i in word_indices:
        x[i] = 1

    return x
