from random import randint
import time

# ���� ���� ��������
def input_name(num):
    print("������� ��� {:d}-�� ��������� ".format(num))
    return input()

# ������������� �������� ������ ��������
def throws(namePlayer):
    print('����� �������', namePlayer)
    time.sleep(2)
    points = randint(1, 6)
    print('������:', points)
    return points

# ���� ����
def game_dice(namePlayer1, namePlayer2):
    numOfThrows = int(input("������� ���������� �������\n"))
    summPointsPlayer1 = 0
    summPointsPlayer2 = 0
    for i in range(numOfThrows):
        print("��� ", i + 1)
        summPointsPlayer1 += throws(namePlayer1)
        summPointsPlayer2 += throws(namePlayer2)
    print(namePlayer1, "����: ", summPointsPlayer1)
    print(namePlayer2, "����: ", summPointsPlayer2)
    return [summPointsPlayer1, summPointsPlayer2]

# ����������� ���������� (3 ��������� ��������)
def winner(namePlayer1, namePlayer2, summPointsPlayer1, summPointsPlayer2):
    if summPointsPlayer1 > summPointsPlayer2:
        print('�������', namePlayer1)
    elif summPointsPlayer1 < summPointsPlayer2:
        print('�������', namePlayer2)
    else:
        print('�����')
