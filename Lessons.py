#TODO: Все материалы что мы прошли на первом(1) уроке.
# CTRL + / - сделать коментарий

# int - Целые числа - 123
# str - Строка 'Hello' '123' 'hello' последовательность символов.
# float - Дробные числа 12.3  5.2
# bool - Логические значение True и False
# list -  Списки [1, 2.1 'hello', 'Hello'] Последовательность объектов.
# dict - Словари { 'John' : "+1-23-45", 'bob' : "+1-35-356"} Список пар: "ключ-значение"
# tuple - Кортежи (1, 2.0, "Hello") Последовательность неизменяемых объектов.
# set - Множества {"a", "b"} последовательность уникальных объектов.

# Математические операции:

#  +, -, *, / - операнды
#  **, //, % -
#  + -Прибовление
#  - -Отнимание
#  * -Умножение
#  / -Деление
#  ** -Возведение в степень
#  // -Деление без остатка
#  % -Деление с остатком (Получение остатка от деление)

# Python - это язык со строгой динамической типизацией
# print(5 + 5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 5)
# print(5 ** 5)
# print(5 // 5)
# print(5 % 5)

#TODO: Переменные, создание и использование

# name = 'Sarvar'
# # name- это переменная. Sarvar- это объект.
# last_name = 'Abdusattorov'
# age = 20
# print('Привет меня завут ' + name + last_name + ' мне '+ str(age)+' года')
# print(f'Привет меня завут {name} {last_name} мне {age} года')
# f''''' - форматированная строка (внутрь которого можно внидрить) (Открывать и вставлять или засуноть)

#TODO: Многосторонний ввывод.
# спец символы для переноса строк:
# \n - переход на новую строку
# \t - табуляция 4 пробела (вставить 4 пробела.)

# print('Привет\nКак дела\n\nНормально\tСам как?')
# print('''Привет
# Как дела?
#
# Нормально   Сам как?''')

# input() - функция для получения значений от пользователя.
# username = input('Введите свой username: ')
# print(username)

# print(type(username)) - Показывает какой тип хранится в переменной.

# username = input('Введите свой username: ')
# user_last_name = input('Введите свой user_last_name: ')
# user_age = input('Введите возраст: ')
# year = 2023
# print(f'''
# Имя: {username}
# Фамилия: {user_last_name}
# Мой год рождения: {2023 - int(user_age)} год.
# ''')

# В форматированном строке чтобы сложить или вычитать нужно число-20 и str вставить во внуторь { } - в такие скобки.
# например:
# numbers = '1000'
# print(f''' {2000 - int(numbers)}''')





#TODO:  Все материалы что мы прошли на втором(2) уроке.

# Операторы сравнения. - <,>,=

# > - Больше.
# < - Меньше.
# <= - Меньше или равно.
# >= - Больше или равно.
# == - Равно ли.
# != - Неравно ли.

# num = 15
# num2 = 20
# num3 = 15
# num4 = 25

# print(num == num2) # Равно ли 15 20
# print(num < num4) # 15 мемньше чем 25
# print(num2 > num3) # 20 больше чем 15
# print(num3 <= num4) # 15 меньше или равно 25
# print(num4 >= num3) # 25 больше или равно 15
# text = 'abc'
# text2 = 'abCd'
# print(text > text2)

# ord() - принимает в себя символ, отдает его порядковый номер в таблице ascii.
# print(ord('a'), ord('A'))
# chr() - она принимает в себя порядковый номер, отдает символ из таблицы.
# print(chr(97), chr(65))


# Изменение регистра строк
# Метот - это функция привязанная к определенному классу.

# content = 'HELLO hello HELlo'

# print(content.lower()) #Все символы (Буквы) в нижнем регисторе.
# hello
# print(content.upper()) #Все символы (Буквы) в верхнем регисторе.
# HELLO
# print(content.capitalize()) #Только первый символ строки будет в верхнем регисторе.
# Hello hello
# print(content.swapcase()) #Меняет регистор символов наоборот.
# HELLO-hello
# print(content.title()) #Каждый первый символ каждого слова в верхнем регисторе.
# Hello Hello

# Условия.

# Код читается строго сверху вниз. Поэтому если в блоке if - отдает True тогда он дальше не будет читать (elif не будет читаться.) а перейдет дальше.
"""
if проверка ( ожидаем значение True):
    если проверка вернула значение True
elif проверка ( ожидаем значение True):
    если блок if  не вернул значение True
else:
    если ни одна проверка не вернула значение True

"""

# age = int(input('Введите ваш возраст: '))
#
# if age < 10: Если age(Введенное число) меньше чем 10 то: Ввыводится на экран print
#     print('Меньше 10')
# elif age > 10: Иначе если age(Введенное число) больше чем 10 то: Ввыводится на экран print
#     print('Больше 10')
# else: если age(Введенное число) равна к 10 то: Ввыводится на экран print
#     print('Равно 10')


# weather = input('Какая у вас погода: ').lower()

# DRY = dont repeat yourself
# or - логическое ИЛИ(нужно хоть одно значение True)
# and - логическое И (нужно чтобы все сравнения отдавали True)
# not - отрицание НЕ

# if weather == 'снег':
#     print('У вас холодно')
# elif weather == 'дождь':
#     print('у вас холодно')
# elif weather == 'солнце':
#     print('у вас жарко')
# elif weather == 'ветерок':
#     print('у вас жарко')
# else:
#     print('наверное пойдет')

# if weather == 'снег' or weather == 'дождь':
#     print('У вас холодно')
# elif weather == 'солнце' or weather == 'ветерок':
#     print('у вас жарко')
# else:
#     print('наверное пойдет')


# Админ Никита 123, Доминик 321
# Менеджер Настя 456, Ева 654

# username = input('Введите ваше имя: ').capitalize()
# password = input('Введите ваш пароль: ')
#
# if username and not password:
#     print('Вы забыли ввести пароль')
# elif not username and password:
#     print('Вы забыли ввести имя')
# elif not username and not password:
#     print('Вы забыли ввести имя и пароль')
# elif (username == "Никита" and password == "123") or (username == "Доминик" and password == "321"):
#     print(f"Привет администратор {username}")
# elif (username == "Настя" and password == "456") or (username == "Ева" and password == "654"):
#     print(f"Привет Менеджер {username}")
# else:
#     print("Неверный Имя или Пароль")




#TODO: Все материалы то что мы прошли на втором(3) уроке.

# Списки
# список - это перечисляемый тип данных, который может хранить в себе все другие типы данных.
# картеж - перечисляемый тип данных, значения которого мы не можем менять.

# list_1 = []
# list_2 = list()
#
# print(list_1, list_2)

# Индексы - это элемент списка
# Индексы всегда стартуют с нуля ( 0 ).
# Индексы - это порядковые номера элемента в перечисляемом типе данных, служат для обращения к одельным элементам.
# Если читать индексы с лева на прово то они начинаются с нуля(0)
# А если с право на лева то с Минус один(-1).

# test_list = [1, 1.1, 'hello', True, []]
#              0   1      2       3    4
#             -5  -4     -3      -2   -1

# print(test_list)
# print(test_list[2])
# print(test_list[-2])
# print(test_list)
# TODO: Изменение элемента по индексу.
# test_list[-1] = 'hello world'
# test_list[0] = 'Bye world'
# test_list[2] = []
# print(test_list)


# food_list = ['lavash', 'pizza', 'doshirak']
# Список.append(значение) - добавляет элемент в конец списка.
# Список.isert(индекс, значение) - добавляет элемент в указанный индекс.

# print(food_list)
# .append(значение)
# food_list.append('burger', 123) -  ЭТО НЕПРАВИЛЬНО! Приведет к ошибке.
# food_list.append('burger')
# food_list.append('shashlik')
# print(food_list)


# .insert(индекс, значение)
# food_list.insert((индекс)1, (значение)'lagman')
# food_list.insert(2, 'shourma')
# print(food_list)

# удаление элементов из списков

# список.remove(элемент) - удаляет элемент из списка по его значению.
# список.pop(индекс) - вырезает элемент из списка по его индексу.

# food_list.remove('lavash')
# print(food_list)
#
# item = food_list.pop(-1)
# print(item.capitalize())
#
# print(food_list)


# список.sort() - сортирует список от наименьшего к наибольшему значению. Постоянная сартировка.
# sorted() - временно сортирует список, отдавая новый объект
# numbers = [1, 22, 42, 0, 99, 63, 21, 12, 72]
# print(numbers)
# print(numbers.sort()) - None
# numbers.sort(reverse=True)  # reverse=True - Переворачивает отсартированный список.
# [99, 72, 63, 42, 22, 21, 12, 1, 0]
# print(numbers)
# numbers.sort()
# [0, 1, 12, 21, 22, 42, 63, 72, 99]
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)


# food_list = ['lavash', 'pizza', 'doshirak']
# Проверка на наличие или отсуствие элемента внутри списка.
# in - Есть ли внутри.
# not in - Нет ли внутри.
# TODO:
# if 'lavash' in food_list:
#     food_list.remove('lavash')
# elif 'burder'not in food_list:
#     print('sadasdad')
# Код читается строго сверху вниз. Поэтому если в блоке if - отдает True тогда он дальше не будет читать (elif не будет читаться.) а перейдет дальше.
# if 'burder'not in food_list:
#     food_list.append('burger')
# print(food_list)

# Список из строки
# sample = '123-123-123-123-123-123-123-123'
# строка.split(символ) - разбивает элементы внутри строки на список, по определенному символу.
# print(sample.split())
# Если мы указываем в (split-те) символ которого нету в нашей строке, то вся строка становится одним элементом списка.

# print(sample.split('-'))

# sample_list = sample.split('-')
# print(sample_list)

# ''.join(список) - склеивает элементы списка в строку, разделяя их по указанному символу.
# 123+123 ...  '+'.join(список)
# print('+'.join(sample_list))
# TODO:
"""
for item in items_list:
    code
"""

# sample = '123-123-123-123-123-123-123-123'
# print(sample.split())
# sample_list = sample.split('-')
# count = 0
# for item in sample_list:
#     count = count + 1
#     print(item + '+')
#
# print(count, len(sample_list))
# len() - функция чтобы узнать длину списка.

# Кортеж -

# '1231456789'
# print(list('1231456789')) # Используется для списков.
# list() - Делает каждый символ отдельным элементом списка. Сюда можем дописать какие-то значение.
# ['1', '2', '3', '1', '4', '5', '6', '7', '8', '8']
# print(tuple('1231456789')) # Используется для картежей.
# tuple() - Используется для хранения значения. И сюда мы не можем дописать какие то значение.
# ('1', '2', '3', '1', '4', '5', '6', '7', '8', '8')

# __sizeof__() - Узнает сколько весит та или иная переменная или иное значение.
# print(list('1231456789').__sizeof__())
# 120
# print(tuple('1231456789').__sizeof__())
# 104
# my_list = [5, 3, 2, 4, 1]
# print(len(my_list))
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))




#TODO: Все материалы что мы прошли на четвертом(4) уроке.

# lst = [1,2,3,4,5,6,7,8,9,10]

# for i in lst:
#     print(f"hello {i}")
# range - создает нам псевдосписок с указанными параметры.
# start=0, finish=int, step=1

# lst1 = []
# for i in range(11):
#     lst1.append(i)
# print(lst1)
#
# lst2 = []
# for i in range(5, 16):
#     lst2.append(i)
# print(lst2)
#
# lst3 = []
# for i in range(1, 20, 3):
#     lst3.append(i)
# print(lst3)

# Генераторы списков - создание списка в одну строку.
# lst1_v2 = [i for i in range(11)]
# print(lst1_v2)
#
# lst1_v3 = [i for i in range(13, 38)]
# print(lst1_v3)

# lst3 = [i ** 2 for i in lst1_v2]
# print(lst3)
# TODO:
# evens1 = [i for i in range(0, 101, 2)]
# print(evens1)
#
# evens2 = [i for i in range(101) if i % 2 == 0]
# print(evens2)
#
# odds1 = [i for i in range(1, 101, 2)]
# print(odds1)
#
# odds2 = [i for i in range(101) if i % 2 != 0]
# print(odds2)
# TODO:


# test_str = ''.join([i * 2 for i in 'hello world'])
# print(test_str)

# print(lst)
# print(min(lst)) # Минимальное значение.
# print(max(lst)) # Максимальное значение.
# print(sum(lst)) # Суммирует все элементы.

# Срез - Временное ограничение списка.
# test_list[0:6]
# start=0:finish=конец_списка:step=2
# test_list = [i for i in range(1, 17)]
# print(test_list[:5])
# print(test_list[2:8:3])
# print(test_list[::3])
# print(test_list[::-1])

# test_str = 'Hello World'
# print(test_str[:5])
# print(test_str[::-1])

# Копирование списков.
# метод.copy()
# copied_list = test_list.copy()
# copied_list2 = [i for i in test_list]
# copied_list3 = test_list[::]
# copied_list4 = test_list
# print(copied_list4)
# print(copied_list3)
# print(copied_list2)
# print(test_list)
# print(copied_list)

# Принудительная остановка работы цикла.
# break - Останавливает работу цикла.
# continue - пропускает ход цикла по условию.
# for i in test_list:
#     print(i)
#     if i  == 8:
#         print("Это цифра 8")
#         break
# for i in test_list:
#     print(i)
#     if i  == 8:
#         print("Это цифра 8")
#         continue




#TODO: Все материалы что мы прошли на пятом(5) уроке.
# Цикл с условиями while

# count1 = 0
# while count1 < 10:
#     print(count1)
#     count1 += 1
#
#
# count2 = 10
# while count2 > 0:
#     print(count2)
#     count2 -= 1


# i = 0
# while i <= 100:
#     print(f'Цифра - {i}')
#     i += 1
# else:
#     print('Закончили работу')

# j = 100
# while j >= 0:
#     print(f'Цифра - {j}')
#     j -=1
# else:
#     print('Закончилт работу')

# products = ['apple','orenge','tomato']
# is_running = True
#
# while is_running:
#     user_text = input('Введите действие: ')
#     if user_text == 'stop':
#         print('Процесс окончен')
#         is_running = False
#         # break
#
#     if user_text == 'show':
#         if not products:
#             print('Мне нечего показать.')
#             continue
#         # count = 1
#         for product in products[::2]:
#             print(products.index(product), product, sep='. ')
#             # count += 1
#         continue
#
#     if user_text == 'clear':
#         products.clear()
#         print('Очистили список', products)
#         continue
#
#     if len(user_text.split()) == 2:
#         command, product = user_text.split()
#         if command == 'add':
#             if product not in products:
#                 products.append(product)
#                 print(f'Добавили продукт {product} в список {products}')
#             else:
#                 print(f'Продукт {product} уже в списке {products}')
#         elif command == 'del':
#             if product in products:
#                 products.remove(product)
#                 print(f'Удалили продукт {product} из списка {products}')
#             else:
#                 print(f'Продукта {product} нетк в списке {products}')
#         else:
#             print('Неизвестная команда')
#
#     else:
#         print('для выполнение команды нужно два слова.')




# TODO: Все материалы что мы прошли на шестом(6) уроке.

# Словарь - {} , .dict()
# dict1 = {}
# dict2 = dict()

# print(dict1, dict2)

# sample = {1,1,1,1,1,1,1,1,2} # Множества set()
# # print(sample)
# dict_sample = {
#     "key_1": "123456789",
#     "key_2": 123456789,
#     "key_3": [1, 2, '1', '2']
# }
#
# print(dict_sample)
# # print(dict_sample["key_3"])
# # print(dict_sample["key_4"])
#
# # .get(ключ) -
# # print(dict_sample.get("key_3", 'Нету такого ключа'))
# # print(dict_sample.get("key_4", 'Нету такого ключа'))
#
# dict_sample['key_2'] = {
#     "a": 1,
#     "b": 2
# }
# print(dict_sample)
# dict_sample["key_4"] = "New key-value"
# print(dict_sample)
# new_key_value = {
#     "abc": 123
# }
# # .update({ Принимает (код и славарь) })
# dict_sample.update(new_key_value)
# print(dict_sample)
# # del
# del dict_sample["key_1"]
# print(dict_sample)

# for item in dict_sample:
#     print(item)
# print(dict_sample.keys())
# print(dict_sample.values())
# for item in dict_sample.keys():
#     print(item)
# for value in dict_sample.values():
#     print(value)
#
# test_dict = {}
# for key in dict_sample.keys():
#     test_dict[key] = dict_sample[key]
# print(dict_sample, "dict_sample")
# print(test_dict, "test_dict")
#
# # .items() - забирает и ключи и значение.
# print(dict_sample.items())
#
# for key, value in dict_sample.items():
#     print(key, value)
#



# TODO: Все материалы что мы прошли на седьмом(7) уроке.

# Функция.
# define definition
"""
def имя_функций(аргументы):
    code
"""

# def print_hello():
#     print('hello')
# print_hello()

# Аргументы
# аргументы бывают двух(2) видов, (Обизательные, необизателльные).
# Если вы указываете аргумент просто его иммя то аргумент сразу считается обизательным.

# def say_hello(name):
#     print('hello', name)
#
# username = input("Your name: ")
# say_hello(username)
#
# def say_hell(name = 'Sarvar'):
#     print('hello', name)
#
# username1 = input("Your name: ")
# if username1:
#     say_hell(username1)
# else:
#     say_hell()
#
# def calculate(num1, num2, operator= "+"):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             return "Нельзя делить на ноль"
#         return num1 / num2

# Аргументы:
#       Позиционные
#       Именование
# result = calculate(10, 15, "/") #Позиционные
# print(result)
# result = calculate(operator= "*",num2= 10, num1=15) #Именованные
# print(result)

# def my_sum(objects):
#     result = 0
#     for item in objects:
#         if type(item) not in [int, float]:
#             return
#         result += item
#     return result
# # print(my_sum([1,2,3,4,5,"6",7,8,9])) - В таком случае мы получаем None
# print(my_sum([1,2,3,4,5,6,7,8,9]))
# print(sum([1,2,3,4,5,6,7,8,9]))


# Фанатация типов - chees: str

# Необязательные неограниченные позиционные аргументы.
# Необязательные неограниченные именованные аргументы.
# *args - можно поставить все что угодно
# **kwargs - точно такие же оргументы но мы для них прописываем Имя




# TODO: Все материалы что мы прошли на восьмом(8) уроке.
