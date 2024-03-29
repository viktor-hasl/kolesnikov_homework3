# Viktor Kolesnikov
# Date: 22/02/2024
# Description: Homework 3
# Grodno IT Academy Python 3.11

import re

def pairs(numbers_string):
    #Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    #Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    #Входные данные - строка из чисел, разделенная пробелами.
    #Выходные данные - количество пар.
    #Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.

    # В начале проверяем, чтобы не ввели пустую строку или всего одно число
    if len(numbers_string.replace(" ", '')) < 2:
        return 0
    else:
        # Переводим строку в список
        list_numbers = numbers_string.split(' ')
        # Затем создаем переменную, в которой мы оставляем все элементы без повторений
        set_list_numbers = list(set(list_numbers))
        pairs = 0
        # Пробежим по нашему set списку и проверим сколько раз повторяется каждый элемент
        for i in set_list_numbers:
            count_repeat = list_numbers.count(i)
            # По формуле высчитаем сколько пар, зная количество
            pairs += (count_repeat * (count_repeat - 1)) / 2
            pairs = int(pairs)
        return pairs


def uniques(array):
    # Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    # Элементы нужно выводить в том порядке, в котором они встречаются в списке.

    """Пробегаем по данному списку с помощью цикла for, проверяем количество повторений элементов
    если элемент встречается только один раз, то мы его добавляем в наш предварительно созданный список
    """
    uniques = []
    for i in array:
        if array.count(i) > 1:
            continue
        else:
            uniques.append(i)
    return uniques


def ordered_list(array):
    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Верните полученный список.
    # Задача не проходит тест. Такой вариант решения мог бы быть, но всего с одним исправлением - item == 0 (см ответы)

    """Перебираем наш список, если элемент равен 0 мы его удаляем с помощью .pop,
    а затем, это значение мы добавляем в конец использую .append
    """
    for i in range(0, len(array)):
        if array[i] == 0:
            zero = array.pop(i)  # .pop удаляем из списка, но возвращает его в переменную
            array.append(zero)

    return array



def tuple_to_list(in_tuple):
    #Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.
    """Просто использую list() обернем наш кортеж"""
    lst = list(in_tuple)
    return lst

def euclid(a,b):
    #Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself
    """В начале делаем проверку на наличие 0 в значениях, затем запускаем цикл, который будет работать,
    до момента пока одно из наших значений не будет ровно нулю, в цикле мы делим большее число на меньшее и получаем остаток,
     если остаток равен нулю, то мы нашли общий делитель и выводим последнее число на которое делили
    """
    if a == 0 and b == 0:
        return False
    elif a == 0:
        return b
    elif b == 0:
        return a

    while a != 0 and b != 0:
        if a > b:
            a = a % b
            if a == 0:
                return b
        else:
            b = b % a
            if b == 0:
                return a

#Dictionaries
def cities(input_string):
    #Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    #Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    #Входные данные
    #Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    #В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    #Выходные данные
    #Для каждого из запроса выведите название страны, в котором находится данный город.
    #Пример данных:
    #Входные данные
    #2
    #Russia Moscow Petersburg Novgorod Kaluga
    #Ukraine Kiev Donetsk Odessa
    #3
    #Odessa
    #Moscow
    #Novgorod
    #Выходные данные
    #Ukraine
    #Russia
    #Russia
    #input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nMoscow\nNovgorod"
    #output_string = 'Ukraine\nRussia\nRussia'
    #country_map={}

    country_map = {}
    # Переводим строку в список по переносам
    input_string = input_string.split('\n')
    # Первый элемент у нас будет количество стран
    count_country = int(input_string[0])
    # Тут мы получаем количество городов которые мы будем искать
    count_city = int(input_string[count_country + 1])
    # Запускаем цикл в котором разбираем каждую страну
    for i in range(1, count_country + 1):
        # Получаем список из страны первым элементом и его городов
        list_country = input_string[i].split(' ')
        list_city = []
        # Тут перебираем наш список страны, а все города помещаем в новый список городов
        for y in range(1, len(list_country)):
            list_city.append(list_country[y])
        # В ранее созданный словарь, помещаем ключ название страны, а затем в значение передаем
        # наш список городов
        country_map[list_country[0]] = list_city

    list_ = []
    # Перебираем все города, что нужно отыскать по заданию
    for i in range(-count_city, 0):
        search_city = input_string[i]
        string = ''
        # Перебираем ключи и получаем списки городов
        for key in country_map.keys():
            list_city = country_map[key]
            # Тут мы поверяем, есть ли город, что мы ищем в списке городов
            if search_city in list_city:
                string += key
                string += ' '
        # Добавляем страну в пустой список, редактируя до нужного вывода
        list_.append(string.strip())
        string += '\n'
    # Получившийся список со странами переводи в строку для вывода
    input_string = '\n'.join(list_)
    return input_string

#Sets
def languages(input_string):
    #Задачи для домашней работы
    #Языки
    #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    #Входные данные
    #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    #Пример входных данных:
    #3 # N количество школьников
    #2 # M1 количество языков первого школьника
    #Russian # языки первого школьника
    #English
    #3 # M2 количество языков второго школьника
    #Russian
    #Belarusian
    #English
    #3
    #Russian
    #Italian
    #French
    #Выходные данные
    #В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    #Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    #input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
    #output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'

    lang_repeat = ''
    count_lang_set = 0
    # Переводим в список по переносу наши входные данные
    input_string = input_string.split('\n')
    # Получаем количество детей
    count_children = int(input_string[0])
    # Переводим в строку, чтобы потом избавиться от цифровых значений
    input_string = ' '.join(input_string)
    input_string = (re.sub(r'\d ', '', input_string)).strip()
    input_string = input_string.split(' ')
    # Получился список с языками, его мы переводим во множетсво и получаем, количество языков
    set_lang = set(input_string)
    for i in set_lang:
        # Проверяем если язык повторяется столько же сколько учеников, то этот язык знает каждый ученик
        if input_string.count(i) == count_children:
            count_lang_set += 1  # Количество повторяемых языков
            lang_repeat += i + '\n'
    # Сюда записываем количество языков
    count_lang = len(set_lang)
    # Сюда построчно языки, что вообще изучаются
    lang_set_str = '\n'.join(list(set_lang))

    input_string = f'{count_lang_set}\n{lang_repeat}{count_lang}\n{lang_set_str}'
    return input_string

#Generators
def list_gen(arr1, arr2):
    #Генераторы списков
    #Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
    #пример:

    result = [i + y for i in arr1 for y in arr2]
    return result


#Генераторы словарей
def dict_gen(N):
    #Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.
    result = {key: key ** 3 for key in range(1, N + 1)}
    return result

#Кортежи
def multiplication_table(N):
    #Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
    """"Cоздаем генератор, в которой получаем матрицу, с помощью циклов пробегаем
    по матрице и выводим построчно
    """
    list_ = [[i * j for i in range(N + 1)] for j in range(N + 1)]
    for i in range(0, len(list_)):
        table = ''
        for j in list_[i]:
            table += (str(j) + ' ')
        table = table.strip()
        yield table
