from statistics import median, stdev, mean
from math import fsum
from random import randint

nums10 = [randint(0, 100) for i in range(10)]
print(*nums10)
print("Сумма элементов: ", fsum(nums10))
print("Среднее значение: ", mean(nums10))
print("Медиана: ", median(nums10))
print("Стандартное отклонение: ", stdev(nums10))
print("Случайное число: ", randint(1,100))
