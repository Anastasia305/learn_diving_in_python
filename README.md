# learn_diving_in_python
This course is part of the Python Programming Specialization

# Как работает интерпретатор Python для скриптов
Запуск на исполнение написанных скриптов или модулей производится в пакетном режиме. И выполняется по сложной схеме, которая состоит из следующих этапов:

1) Последовательная обработка всех операторов, которые записаны в скрипте.

2) Компиляция исходного хода в промежуточный формат. Интерпретатор создает байт-код, который представляет собой язык программирования низкого уровня, независимый от платформы и операционной системы. Байт-код необходим для оптимизации процесса выполнения скрипта.

3) Исполнение полученного кода. На этом этапе вступает в действие виртуальная машина Python (PVM), которая циклично перебирает каждый оператор из скрипта и запускает его на исполнение. Как будто вы вводите каждую команду последовательно в интерактивном интерпретаторе.

REPL (от англ. read-eval-print loop — «цикл „чтение — вычисление — вывод“») — форма организации простой интерактивной среды программирования в рамках средств интерфейса командной строки. 
## Useful links
[Документация Python](https://docs.python.org/3/)

[PEP8](https://www.python.org/dev/peps/pep-0008/)

[Утилита autopep8,](https://pypi.org/project/autopep8/)

[Коллекция полезных библиотек](https://github.com/vinta/awesome-python)

# Basic types and constructions 
## Численные типы:
int (целые числа)

```
num = 13
print(type(num))
<class 'int'>
```
float (вещественные числа):
```
num = 13.4
num = 1.5e2 #экспоненциальная нотация
```
### Конвертация типов
int -> float

### Комплексные числа(complex)
```
num = 14 + 1j
```

*Модуль **decimal** для работы с вещественными числами с фиксированной точностью*

*Модуль **fractions** для работы с рациональными числами*


### Основные операции с числами
Целое и вещественное число дает вещественное число при сложении/вычетании

Деление  - прямой слэш(/), результат всегда вещественный.

Возведение в степень **

Целочисленное деление //
```
10 // 3
```

Остаток деления %
```
10 % 3
1
```
**Побитовые операции????*** 

## *Задача*
Найти расстояние между двумя точками в декартовых координатах.

## *Решение*
```
>>> x1, y1 = 0, 0
>>> x2 = 3
>>> y2 = 4
>>> distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
>>> distance
5.0
```
Меняем местами значения 2-ч переменных
```
>>> a = 100
>>> b = 200
>>> print(a, b)
100 200
>>> a, b = b, a
>>> print(a, b)
200 100
```

## mutable и immutable types
Числа - неизменяемы тип данных 
```
x = y = 0
x += 1

print(x)
print(y)
1
0
```
Списки изменяемый тип данных
```
x = y = []
x.append(1)
x.appensd(2)
print(x)
print(y)
[1, 2]
[1, 2]
```

## Логические типы (bool)
*Конвертация типов*
```
bool(12)
True
bool(0)
False
```
### Логические выражения
Логическая "и":
```
x, y = True, False
print(x and y)

False
```

Логическое "или":
```
x, y = True, False
print(x or y)

True
```

Логическое отрицание:
```
y = False
print(not y)
True
```

Составные логические выражения:
```
x, y, z = True, False, True
result = x and y or z
print(result)

True
```

```
x = 12
y = False

print(x or y)

12
```

```
x = 12
z = 'boom'

print(x and z)

boom
```

## *Задача*

Определить високосный год или нет?
Год является високосным если он кратен 4. но при этом не кратен 100, либо кратен 400.

## *Решение*

```
>>> year = 2017
>>> is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
>>> print(is_leap)
False

```

```
>>> import calendar
>>> print(calendar.isleap(1980))
True

``` 
Python - это язык, у которго батарейки включены.

## Строки и байтовые строки
Экранирование символов

```
>>> example_string = "Курс про \"Python\" на \"Coursera\""
>>> print(example_string)
Курс про "Python" на "Coursera"

```

## "Сырые" строки (r-строки):

```
>>> example_string = r"Файл на диске c:\\"
>>> print(example_string)
Файл на диске c:\\

```

Как разбить длинную строку

```
>>> example_string = "Perl - это тот язык, который одинаково " \
...                  "выглядит как до, так и после RSA шифрования." \
...                  "(Keith Bostic)"
>>> print(example_string)
Perl - это тот язык, который одинаково выглядит как до, так и после RSA шифрования.(Keith Bostic)
```

или использовать """


Как объединить 2 строки в одну?
"" + ""


СЬроки можно умножать

## строки неизменяемые

```
>>> example_string = "Привет"
>>> print(id(example_string))
2328907491568
>>> example_string += ", Мир!"
>>> print(id(example_string))
2328916091264
```

Когда мы изменили строку, на самом деле, мы создали новый строковый объект.

##Срезы строк [start:stop:step]

##Строковые методы
quote = """Болтовня ничего не стоит. Покажите мне код.
Linus Torvalds
"""

guote.count("0")
6

.capitalize() - делает первую букву в строке заглавной
.isdigit() - проверяет является ли строка числои и возвращает булевое значение

## Оператор in

```
>>> "3.14" in "Число Пи = 3.1415926"
True
```

## for .. in

```

>>> example_string = "Привет"
>>> for letter in example_string:
...     print("Буква", letter)
...
Буква П
Буква р
Буква и
Буква в
Буква е
Буква т

```

Непустая строка при конвертации в bool даст True, пустая False.

## Форматирование строк

1-ый способ:

```

>>> template = "%s - главное достоинство программиста. (%s)"
>>> template % ("Лень", "Larry Wall")
'Лень - главное достоинство программиста. (Larry Wall)'

```

 %s - placeholder строки
 %d - целое число
 
 
 2-ой способ:
 
 ```
 >>> "{} не лгут, но {} пользуются формулами. ({})".format(
...     "Цифры", "лжецы", "Robert A. Heinlein"
... )
'Цифры не лгут, но лжецы пользуются формулами. (Robert A. Heinlein)'

```

Так же можно использовать именованые аргуметны.


f-строки:
f"{}"

## Модификаторы форматирования:

```
>>> num = 8
>>> f"Binary: {num:#b}"
'Binary: 0b1000'

```

```

>>> num = 2/3
>>> print(num)
0.6666666666666666
>>> print(f"{num:.3f}")
0.667

```

## Втроенная функция input()


## Объект None
None - это объект специального типа NoneType, который нужен для обозначения отсутствия значения(аналогично нулевому указателю в С).

```
>>> answer = None
>>> print(type(None))
<class 'NoneType'>
>>> bool(None)
False
>>> answer = None
>>> if not answer:
...     print("Ответ не получен")
...
Ответ не получен
>>> income = 0
>>> if not income:
...     print("Ничего не заработали")
...
Ничего не заработали
>>> income = None
>>> if income is None:
...     print("Еще не начали продавать")
... elif not income:
...    print("Ничего не заработали")
...
Еще не начали продавать

```

## Управление потоком

### if - проверка условия
Оператор if используется для выполнения каких-либо действий при выполнении условия.

```
>>> company = "my.com"
>>> if "my" in company:
...    print("Условие выполнено")
...
Условие выполнено

>>> company = "example.net"
>>> if "my" in company or company.endswith(".net"):
...    print("Условие выполнено")
...
Условие выполнено

```

### if - else
Оператор else позволяет выполнить какой-либо код, если условие в блоке if не выполнилось.

```
company = "google.com"

if "my" in company:
    print("Условие выполнено!")
else:
    print("Условие не выполнено!")

Условие не выполнено!

```

### if - elif - else
Понятно.

## Аналог тернарного оператора

```
>>> score_1 = 5
>>> score_2 = 0
>>> winner = "Argentina" if score_1 > score_2 else "Jamaica"
>>> print(winner)
Argentina

```

## while

```
>>> i = 0
>>> while i < 100:
...    i += 1
...
>>> print(i)
100

```

## Оператор continue

```
>>> result = 0
>>> for i in range(10):
...     if i % 2 != 0:
...         continue
...     result += i
...     print(result)
...
0
2
6
12
20

```

## Объектная структура в Python

Когда мы создаем переменную, мы не просто присваиваем переменной значение, а мы создаем связь имени переменной с объектом.
В Python переменная ссылается на объект, и если мы посмотрим внимательней на наш объект и используем функцию dir для того, чтобы посмотреть все методы атрибута, то мы увидим, что на самом деле их еще больше, чем мы могли бы подумать

```
>>> num = 13
>>> num.__add__(2)
15
>>> print(dir(num))
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> print(dir("string"))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>

```

В Python всё есть объект. Целые числа, строки — это все представлено, как объект внутри. На оси уровня определена структура, которая называется PyObject. Эта структура содержит два важных поля, первое из которых это ob_refcnt — это счетчик ссылок. 



 
 






