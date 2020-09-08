import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v3(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
       больше оно или меньше нужного. Величина приращения значения прогноза зависит от предыдущих попыток и
       вычисляется как среднее арифметическое между текущим и предыдущим значением прогноза.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)     # прогноз
    left = 0                                # левая граница диапазона поиска
    right = 101                             # правая граница диапазона поиска
    while number != predict:
        count += 1
        if number > predict:
            left = predict
            predict += (right - predict) // 2
        elif number < predict:
            right = predict
            predict -= (predict - left) // 2
    return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
