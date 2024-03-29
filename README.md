# kolesnikov_homework3
### Viktor Kolesnikov
### Date: 22/02/2024
### Description: Homework 3
### Grodno IT Academy Python 3.11

Выполняя домашнее задание использовал только библиотку ```re``` для того чтобы убрать ненужные элементы со строки.

#### Задача 1:
>Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
>Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
>Входные данные - строка из чисел, разделенная пробелами.
>Выходные данные - количество пар.
>Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.

Для решения данной задачи, я использовал списки и множество, искал элементы которые повторяются, а затем 
если они повторяются я по фурмуле ```пары = (количесвто_элементов * (количество_элементов - 1)) / 2```

#### Задача 2:
>Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
>Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Пробегаем по данному списку с помощью цикла ```for```, проверяем количество повторений элементов,
если элемент встречается только один раз, то мы его добавляем в наш предварительно созданный список

#### Задача 3:
>Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
>не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
>дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
>Верните полученный список.
>Задача не проходит тест. Такой вариант решения мог бы быть, но всего с одним исправлением - ```item == 0``` (см ответы)

Перебираем наш список, если элемент равен `0` мы его удаляем с помощью ```.pop```, а затем, это значение мы добавляем в конец использую ```.append```

#### Задача 4:
>Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.

Просто использую ```list()``` обернем наш кортеж

#### Задача 5:
>Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию).

В начале делаем проверку на наличие нуля в значениях, затем запускаем цикл, который будет работать,
до момента пока одно из наших значений не будет ровно нулю, в цикле мы делим большее число на меньшее и получаем остаток,
если остаток равен нулю, то мы нашли общий делитель и выводим последнее число на которое делили


#### Задача 6:
>Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
>Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
>Входные данные
>Программа получает на вход количество стран `N`. Далее идет `N` строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
>В следующей строке записано число `M`, далее идут `M` запросов — названия каких-то `M` городов, перечисленных выше.
>Выходные данные
>Для каждого из запроса выведите название страны, в котором находится данный город.

Очень объемная задача, в начале я разбил данную строку на список, получил количтво странн, и странны с ее городами, затем разбил эти странны по спискам 
и добавил в словарь, искомые города я проверял в каждом ключе(в каждой странее)

#### Задача 7:
>Каждый из N школьников некоторой школы знает `Mi` языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
>Входные данные
>Первая строка входных данных содержит количество школьников `N`. Далее идет `N` чисел `Mi`, после каждого из чисел идет `Mi` строк, содержащих названия языков, которые знает `i-й` школьник.

Получаемую строку разделил по переносам, вывел количество учеников, сделав множетсво я получил сколько всего языков, потом проверял сколько раз язык повторяется, если столько же сколько и 
учеников делаем вывод, что каждый ученик владеет им, так пройдясь по каждому языку в конце мы получаем ,сколько всего языков , какие знают все ученики и сколько их

#### Задача 8:
>Используйте генератор списков чтобы получить следующий: `['xy', 'xz', 'xv', 'yy', 'yz', 'yv']`. из `['x','y'] & ['y','z','v']`

Просто в генераторе перебирая два списка мы складываем значения

#### Задача 9:
>Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от `1 до N`, а значениями кубы этих чисел.

Используем генератор слоравей и там возводим значение в степень

#### Задача 10:
>Создайте генератор, который возвращает строки таблицы умножения от `0` до заданного числа.

Cоздаем генератор, в которой получаем матрицу, с помощью циклов пробегаем
по матрице и выводим построчно
   
