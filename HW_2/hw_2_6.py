"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""


def game(num, i=0):
    answer = int(input('Введите число: '))
    counter = 10
    if i == counter - 1:
        return 'Вы проиграли!'
    elif answer == num:
        return f'Вы угадали!\nЗагаданное число: {num}'
    else:

        if answer > num:
            print(f'Вы ввели слишком большое число\nОсталось {counter - i - 1} попыток')
            return game(num, i + 1)
        else:
            print(f'Вы ввели слишком маленькое число\nОсталось {counter - i - 1} попыток')
            return game(num, i + 1)


print(game(40))
