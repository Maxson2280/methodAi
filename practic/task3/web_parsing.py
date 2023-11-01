from bs4 import BeautifulSoup as bs
import codecs
# открываем документ
doc = bs(codecs.open('pars_site.htm', encoding='utf-8', mode='r').read(), 'html.parser')
# извлечение данных из статьи
author = doc.select('.tm-user-card__name_variant-article')[0].decode_contents().strip()
title = doc.select('.tm-title')[0].text.strip()
date = doc.select('.tm-article-datetime-published')[0].text.strip()
tags = list(map(lambda x: x.text.strip(), doc.select('.tm-tags-list__link')))
rating = int(doc.select('div.tm-article-rating span.tm-votes-meter__value')[0].decode_contents().strip())

# вывод на экран
print('Автор:', author)
print('Заголовок:', title)
print('Дата:', date)
print('Теги:', tags)
print('Рейтинг:', rating)
# извлечение данных о комментариях
comments = []
for node in doc.select('div.tm-article-blocks__comments'):
    text = node.select('div.tm-comment__body-content')[0].decode_contents().strip()
    rating = int(node.select('.tm-votes-meter__value tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-comment tm-votes-meter__value_rating')[0].decode_contents().strip())
    author = node.select('.tm-user-info__user_appearance-default')[0].decode_contents().strip()
    comments.append({'text': text, 'rating': rating, 'author': author})
# вывод информации по комментариям
print('Комментариев в статье: ', len(comments))
print('Самый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])
most_popular = sorted(comments, key=lambda x: x['rating'], reverse=True)[0]
print('Самый популярный комментарий:', most_popular['text'], 'Рейтинг ', most_popular['rating'])
# самый активный комментатор
commentators = {}
for comment in comments:
    if comment['author'] in commentators:
        commentators[comment['author']] += 1
    else:
        commentators[comment['author']] = 1
most_active = max(commentators, key=commentators.get)
print('Самый активный:', most_active, ', комментариев:', commentators[most_active])