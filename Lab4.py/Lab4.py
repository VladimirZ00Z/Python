from random import randint
import time

# ���� ���� ��������
igrok1 = input('������� ��� 1-�� ��������� ')
igrok2 = input('������� ��� 2-�� ��������� ')
summPointsIgrok1 = 0
summPointsIgrok2 = 0

for i in range(5):
    # ������������� �������� ������ ������ ��������
    print("��� ", i + 1)
    print('����� �������', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('������:', n1)
    summPointsIgrok1 += n1
    # ������������� �������� ������ ������ ��������
    print('����� �������', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('������:', n2)
    summPointsIgrok2 += n2

print(igrok1, "����: ", summPointsIgrok1)
print(igrok2, "����: ", summPointsIgrok2)
# ����������� ���������� (3 ��������� ��������)
if summPointsIgrok1 > summPointsIgrok2:
    print('�������', igrok1)
elif summPointsIgrok1 < summPointsIgrok2:
    print('�������', igrok2)
else:
    print('�����')
