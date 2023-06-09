"""Игра угадай число 3.0
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 #счетчик попыток
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    predict_number_lst = [0] #создаем список для отслеживания чисел, 
    #которые не соответствуют загаданному числу
    
    while True:
        count += 1
        if predict_number == number:
            break #число найдено
        elif predict_number in predict_number_lst: #если предполагаемое число уже встречалось, то оно увеличивается на единицу
            predict_number += 1
        elif predict_number > number:
            predict_number_lst.append(predict_number)
            predict_number //= 2
        elif predict_number < number:
            predict_number_lst.append(predict_number)
            predict_number += 2
       
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score



if __name__ == "__main__":
    # RUN
    score_game(random_predict)
