from random import *


def is_valid(x):
    return x.isdigit() and 1 <= int(x) <= 100

def game():
    number = randint(1, 101)
    print('Добро пожаловать в числовую угадайку')
    count = 1
    while True:
        n = input('Введите число от 1 до 100: ')
        if is_valid(n) == False:
            print("А может быть всё таки введём число от 1 до 100?")
        else:
            n = int(n)
            if n < number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
                continue
            elif n > number:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
                continue
            elif n == number:
                print('Вы угадали, поздравляем!')
                print('Совершено попыток:', count)
                break
    print('Начать заново? (Да\Нет)')
    answer = input()
    if answer == 'Нет':
        print('Спасибо, что играли в числовую угадайку')
    else:
        while answer == 'Да':
            game()

game()
