from statistics import median, stdev, mean
from math import fsum
from random import randint

nums10 = [randint(0, 100) for i in range(10)]
print(*nums10)
print("����� ���������: ", fsum(nums10))
print("������� ��������: ", mean(nums10))
print("�������: ", median(nums10))
print("����������� ����������: ", stdev(nums10))
print("��������� �����: ", randint(1,100))
