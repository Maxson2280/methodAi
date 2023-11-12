import numpy as np
import scipy.io
from sklearn import svm
from collections import OrderedDict
from process_email import process_email
from process_email import email_features
from process_email import get_dictionary

with open('../../Metodichka/lab/lab2/email.txt', 'r') as file:
    email = file.read().replace('\n', '')
    print(email)
#task2
word_indices = process_email(email)
print(word_indices)
#task3
features = email_features(word_indices)
print(f"Длина вектора признаков: {len(np.array(features))}")
print("Количество ненулевых элементов: {}".format(sum(np.array(word_indices) > 0)))
#task4
data = scipy.io.loadmat('train.mat')
X = data['X']
y = data['y'].flatten()
print('Тренировка SVM-классификатора с линейным ядром...')

clf = svm.SVC(C=0.1, kernel='linear', tol=1e-3)
model = clf.fit(X, y)
p = model.predict(X)
# Оценка точности
accuracy = np.mean(p == y)
# Вывод точности классификации на обучающей выборке в процентах
print(f'Точность на обучающей выборке: {accuracy * 100:.3f}%')
#task5
data = scipy.io.loadmat('test.mat')
X = data['Xtest']
y = data['ytest'].flatten()
print('Предсказание на тестовой выборке: ')
p = model.predict(X)
# Оценка точности
accuracy = np.mean(p == y)
# Вывод точности классификации на обучающей выборке в процентах
print(f'Точность на тестовой выборке: {accuracy * 100:.3f}%')
#task6
t = sorted(list(enumerate(model.coef_[0])),key=lambda e: e[1], reverse=True)
d = OrderedDict(t)
idx = list(d.keys())
weight = list(d.values())
dictionary = get_dictionary()
print('Топ-15 слов в письмах со спамом: ')
for i in range(15):
    print(' %-15s (%f)' %(dictionary[idx[i]], weight[i]))
# вывод: в спам зачастую попадают письма, с рекламными предложениями которые содержат в себе слова которые представлены в консоли
#task7

# Загрузка и предобработка письма
with open('C:/Users/makim/Desktop/methodAi/labs/labs2/mye-mail/good_email.txt', 'r') as file:
    good_email = file.read().replace('\n', '')
with open('C:/Users/makim/Desktop/methodAi/labs/labs2/mye-mail/spam_email.txt', 'r', encoding='utf-8') as file:
    spam_email = file.read().replace('\n', '')


good_indices = process_email(good_email)
spam_indices = process_email(spam_email)

# Создание векторов признаков
good_features = email_features(good_indices)
spam_features = email_features(spam_indices)

# Проход через модель
good_prediction = model.predict(good_features.reshape(1, -1))
spam_prediction = model.predict(spam_features.reshape(1, -1))

# Печать результатов
print("Прогноз для хорошего письма:", good_prediction)
print("Прогноз для спама:", spam_prediction)

