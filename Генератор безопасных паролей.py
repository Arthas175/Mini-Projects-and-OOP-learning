from random import *


def count():
    cntPw = input('Укажите количество паролей для генерации:')
    while cntPw.isdigit() == False:
        print('Нужно вводить цифру')
        cntPw = input('Укажите количество паролей для генерации:')
    return int(cntPw)

def lenght():
    lenPw = input('Укажите длину одного пароля')
    while lenPw.isdigit() == False:
        print('Введите число')
        lenPw = input('Укажите длину одного пароля')
    return int(lenPw)

def digits():
    digPw = input('Включать ли цифры для генерации паролей? (д или н)')
    while digPw.lower() not in ['д', 'н']:
        print('Нужно вводить "д" или "н"')
        digPw = input('Включать ли цифры для генерации паролей? (д или н)')
    return digPw

def abc():
    abcPw = input('Включать ли прописные буквы? (д или н)')
    while abcPw.lower() not in ['д', 'н']:
        print('Нужно вводить "д" или "н"')
        abcPw = input('Включать ли прописные буквы? (д или н)')
    return abcPw

def ABC():
    ABCPw = input('Включать ли строчные буквы? (д или н)')
    while ABCPw.lower() not in ['д', 'н']:
        print('Нужно вводить "д" или "н"')
        ABCPw = input('Включать ли строчные буквы? (д или н)')
    return ABCPw

def punctuation():
    pctPw = input('Включать ли символы? (д или н)')
    while pctPw.lower() not in ['д', 'н']:
        print('Нужно вводить "д" или "н"')
        pctPw = input('Включать ли символы? (д или н)')
    return pctPw

def ambigiuous():
    excPw = input('Исключать ли неодназначные символы? (д или н)')
    while excPw.lower() not in ['д', 'н']:
        print('Нужно вводить "д" или "н"')
        excPw = input('Включать ли символы? (д или н)')
    return excPw

def gen_chars():
    chars = ''
    if digPw == 'д':
        chars += '0123456789'
    if abcPw == 'д':
        chars += 'abcdefghijklmnoprstuvwxyz'
    if ABCPw == 'д':
        chars += 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    if pctPw == 'д':
        chars += '!#$%&*+-=?@^_'
    if excPw == 'д':
        for c in 'iI1Lo0O':
            chars.replace(c, '')
    return chars

def generate_password():
    for i in range(cntPw):
        password = []
        for j in range(lenPw):
            password.append(choice(chars))
        print(''.join(password))

cntPw = count()
lenPw = lenght()
digPw = digits()
abcPw = abc()
ABCPw = ABC()
pctPw = punctuation()
excPw = ambigiuous()
chars = gen_chars()
generate_password()



