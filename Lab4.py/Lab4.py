from random import randint
import time

# Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
summPointsIgrok1 = 0
summPointsIgrok2 = 0

for i in range(5):
    # Моделирование бросания кубика первым играющим
    print("Шаг ", i + 1)
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    summPointsIgrok1 += n1
    # Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    summPointsIgrok2 += n2

print(igrok1, "очки: ", summPointsIgrok1)
print(igrok2, "очки: ", summPointsIgrok2)
# Определение результата (3 возможных варианта)
if summPointsIgrok1 > summPointsIgrok2:
    print('Выиграл', igrok1)
elif summPointsIgrok1 < summPointsIgrok2:
    print('Выиграл', igrok2)
else:
    print('Ничья')
