#Работа со строками
string1 = "This is a string."
string2 = " This is another string."
print(string1+string2)
print(string1)
print(len(string1))
print(string1.title())
print(string1.lower())
print(string2.upper())
print(string1.rstrip())
print(string2.lstrip())
print(string1.strip())
print(string1.strip("0"))

#Извлечение символов и подстрок
d = "qwerty"
ch = d[2]
print(ch, d[1:3], d[1:], d[:3], d[:], d[1:5:2], sep = "; ")
d[2] = 'o' #ошибка

#Работа с числами
intNum1 = 14
intNum2 = 5
print(intNum1//intNum2, intNum1%intNum2, intNum1**intNum2)

#Преобразование данных
param = "string" + str(15)
print(param)

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print("{:7.3f}  plus  {:7.3f} =  {:7.3f}".format(float(n1), float(n2), n3))

#Форматирование строк
a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

#Списки
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

list1[3] = 7
list1.append(13)
list1.insert(1, 5)
list1.pop(1)
list1.pop(len(list1) - 1)
print(list1)

#Сортировка элементов списка
list1.sort(reverse=True)
print(list1)

list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(list2)
print(lis)

#Кортежи
print(dir(tuple))
help(tuple.index)
help(tuple.count)

seq = (2,8,23,97,92,44,17,39,11,12)
print(seq.count(8))
print(seq.index(44))
listseq = list(seq)
print(type(listseq))
print(listseq)
listseq.sort()
listseq.append(17)
print(listseq)

#Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 10
print(D['quantity'])

dp = {}
dp['name'] = input('Введите имя:')
dp['age'] = input('Введите возраст:')
print(dp)
#Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
 'job': ['dev', 'mgr'],
 'age': 25}

print(rec['name']['firstname'], ' ',rec['name']['lastname'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)
