import random

def is_valid(str_number, upper):
    return str_number.isdigit() and len(str_number) > 0 and 1 <= int(str_number) <= upper

def guess(a, b):
    
    hidden_number = random.randint(a, b)
    print(f'Попробуйте угадать число от {a} до {b}')
    counter = 0

    while True:
        
        print('Введите число: ', end = '')
        str_number = input()

        if not is_valid(str_number, b):
            print(f'А может быть все-таки введем целое число от 1 до {b}?')
            continue

        number = int(str_number)
        counter += 1

        if number < hidden_number:
            print('Ваше число меньше загаданного, попробуйте еще разок: ')
        elif number > hidden_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали за {counter} попытки, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

a = 1

print('Добро пожаловать в числовую угадайку!')
print('Введите максимальное число, которое мы загадаем для вас: ', end = '')
b = int(input())

while True:
    guess(a, b)
    print('Хотите сьиграть еще раз?. yes (y)', end = '')
    if input() != 'y':
        break

