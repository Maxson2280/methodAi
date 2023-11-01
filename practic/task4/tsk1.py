import math
import matplotlib.pyplot as plt
from recommendations import critics
from math import sqrt

# Фильмы
film1 = 'Каникулы в Простоквашино'
film2 = 'Ёжик в тумане'

# Список критиков, оценивших оба фильма
common_critics = [critic for critic in critics if film1 in critics[critic] and film2 in critics[critic]]

# Оценки для фильмов
ratings_film1 = [critics[critic][film1] for critic in common_critics]
ratings_film2 = [critics[critic][film2] for critic in common_critics]

# Построим диаграмму рассеяния
plt.figure(figsize=(6, 6))
plt.scatter(ratings_film1, ratings_film2, color='red')
plt.title(f'Оценки критиков')
plt.xlabel(f'Оценки для "{film1}"')
plt.ylabel(f'Оценки для "{film2}"')

# Добавим подписи для критиков
for i, critic in enumerate(common_critics):
    plt.annotate(critic, (ratings_film1[i], ratings_film2[i]), textcoords="offset points", xytext=(0,10), ha='center', bbox=dict(boxstyle='round', facecolor='white'))

plt.grid(True)

plt.xlim(0, 5)
plt.ylim(0, 5)

plt.show()

#task1 euclidean distance

# Функция для вычисления евклидова расстояния
def euclidean_distance(critic1, critic2):
    common_movies = set(critic1.keys()) & set(critic2.keys())
    if not common_movies:
        return None

    distance = 0
    for movie in common_movies:
        distance += (critic1[movie] - critic2[movie]) ** 2

    return sqrt(distance)


# Функция для вычисления меры близости
def similarity_measure(distance):
    if distance is None:
        return 0
    return 1 / (1 + distance)


# Функция для отметки точек критиков на координатной плоскости
def plot_points(critics):

    for critic, ratings in critics.items():
        x = ratings.get('Ну, погоди!', 0)
        y = ratings.get('Котёнок по имени Гав', 0)
        plt.scatter(x, y, label=critic)

    plt.xlabel('Оценка для "Ну, погоди!"')
    plt.ylabel('Оценка для "Котёнок по имени Гав"')
    plt.legend()
    plt.show()


# Применяем функции к данным
critic1 = critics['Кот Матроскин']
critic2 = critics['Пёс Шарик']

distance = euclidean_distance(critic1, critic2)
similarity = similarity_measure(distance)

print(f'Мера близости между Кот Матроскин и Пёс Шарик: {similarity}')

# Отмечаем точки критиков на координатной плоскости
plot_points(critics)

#task2

import math


def euclidean_distance(critic1, critic2):
    common_movies = set(critic1.keys()) & set(critic2.keys())
    if not common_movies:
        return None

    distance = math.sqrt(sum((critic1[movie] - critic2[movie]) ** 2 for movie in common_movies))
    return distance


def similarity_score1(critic1, critic2):
    distance = euclidean_distance(critic1, critic2)
    if distance is None:
        return 0
    n = len(critic1)
    p = math.sqrt(distance / n)
    return 1 / (1 + p)


def similarity_score2(critic1, critic2):
    distance = euclidean_distance(critic1, critic2)
    if distance is None:
        return 0
    n = len(critic1)
    p = math.sqrt(distance / n)
    return 1 / (1 + math.sqrt(p))


if __name__ == '__main__':
    critic1 = critics['Кот Матроскин']
    critic2 = critics['Пёс Шарик']

    euclidean_dist = euclidean_distance(critic1, critic2)
    sim_score1 = similarity_score1(critic1, critic2)
    sim_score2 = similarity_score2(critic1, critic2)

    print(f"Евклидово расстояние: {euclidean_dist}")
    print(f"Мера близости (формула 1): {sim_score1}")
    print(f"Мера близости (формула 2): {sim_score2}")
#task3


