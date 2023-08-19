whats_direction = input('Что нужно сделать?: шифровать или дешифровать? (Нужно ввести "шифровать" или "дешифровать)"').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Нужно ввести "шифровать" или "дешифровать')


whats_language = input('Язык для шифрования или дешифрования: "рус" или "англ"').lower()
while whats_language != 'рус' and whats_language != 'англ':
    whats_language = input('Нужно ввести "рус" или "англ"')


step_count = input('Сдвиг на сколько шагов?: ')
while step_count.isdigit() == False:
    step_count = input('Введите число')


whats_text = input('Введите то, что нужно зашифровать или дешифровать')


def caesar(direction, language, step, text):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for i in range(len(text)):
        if language == 'рус':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alpabet = upper_rus_alphabet
        if language == 'англ':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alpabet = upper_eng_alphabet
        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alpabet.index(text[i])
            if direction == 'дешифровать':
                index = (place - int(step)) % alphas
            elif direction == 'шифровать':
                index = (place + int(step)) % alphas
            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alpabet[index], end='')
        else:
            print(text[i], end='')


caesar(whats_direction, whats_language, step_count, whats_text)
