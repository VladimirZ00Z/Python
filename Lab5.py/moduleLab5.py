from random import randint
import time

# Ввод имен играющих
def input_name(num):
    print("Введите имя {:d}-го играющего ".format(num))
    return input()

# Моделирование бросания кубика играющим
def throws(namePlayer):
    print('Кубик бросает', namePlayer)
    time.sleep(2)
    points = randint(1, 6)
    print('Выпало:', points)
    return points

# Ядро игры
def game_dice(namePlayer1, namePlayer2):
    numOfThrows = int(input("Введите количество бросков\n"))
    summPointsPlayer1 = 0
    summPointsPlayer2 = 0
    for i in range(numOfThrows):
        print("Шаг ", i + 1)
        summPointsPlayer1 += throws(namePlayer1)
        summPointsPlayer2 += throws(namePlayer2)
    print(namePlayer1, "очки: ", summPointsPlayer1)
    print(namePlayer2, "очки: ", summPointsPlayer2)
    return [summPointsPlayer1, summPointsPlayer2]

# Определение результата (3 возможных варианта)
def winner(namePlayer1, namePlayer2, summPointsPlayer1, summPointsPlayer2):
    if summPointsPlayer1 > summPointsPlayer2:
        print('Выиграл', namePlayer1)
    elif summPointsPlayer1 < summPointsPlayer2:
        print('Выиграл', namePlayer2)
    else:
        print('Ничья')
