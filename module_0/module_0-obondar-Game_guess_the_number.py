import numpy as np


def game_core_v3(number):

    '''Устанавливаем верхнюю и нижнюю границы поиска, делим отрезок на половину.
       Сравниваем больше или меньше это загаданного числа.
       Изменяем границы поиска и так же делим отрезок пополам.
       Пока не будет найдено загаданное число.'''

    count = 1
    upper_bound = 101
    lower_bound = 1
    predict = upper_bound // 2

    while number != predict:
        count += 1
        if number > predict:
            lower_bound = predict
            predict = (upper_bound-lower_bound)//2 + lower_bound
        else:
            upper_bound = predict
            predict = (upper_bound-lower_bound)//2 + lower_bound

    return (count)  # выход из цикла, если угадали


def score_game(game_core):

    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# Проверяем
score_game(game_core_v3)
