import random

def is_valid(n):
    return str_number.isdigit() and len(str_number) > 0 and 1 <= int(n) <= 100

a, b = 1, 100

hidden_number = random.randint(a, b)
print('Добро пожаловать в числовую угадайку!')
print(f'Попробуйте угадать число от {a} до {b}')

while True:
    print('Введите число: ', end = '')
    
    str_number = input()
    if not is_valid(str_number):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    number = int(str_number)

    if number < hidden_number:
        print('Ваше число меньше загаданного, попробуйте еще разок: ')
    elif number > hidden_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
