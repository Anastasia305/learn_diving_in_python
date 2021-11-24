#!/usr/bin/env python3

#standard library
import random


number = random.randint(0, 100)


while True:
    answer = input('Угадайте число:\n')
    if answer == '' or answer == 'exit':
        print('Выход из программы')
        break

    if not answer.isdigit():
        print('введите приавильное число')
        continue

    answer = int(answer)

    if answer == number:
        print('Совершенно верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')


