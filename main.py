from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def count_password():
    count = input('Какое количество паролей вам необходимо? ')
    while not count.isdigit():
        print('Введите цифру!')
        count = input('Какое количество паролей вам необходимо? ')
    return int(count)


def len_password():
    l = input('Длина вашего пароля? ')
    while not l.isdigit():
        print('Введите цифру!')
        l = input('Длина вашего пароля? ')
    return int(l)


def q1_pas():
    q1 = input('Включать ли цифры 0123456789 ?').lower()
    while q1 not in ['да', 'нет']:
        print('Введите только да или нет')
        q1 = input('Включать ли цифры 0123456789 ?').lower()
    return q1


def q2_pas():
    q2 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?').lower()
    while q2 not in ['да', 'нет']:
        print('Введите только да или нет')
        q2 = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ?').lower()
    return q2


def q3_pas():
    q3 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?').lower()
    while q3 not in ['да', 'нет']:
        print('Введите только да или нет')
        q3 = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ?').lower()
    return q3


def q4_pas():
    q4 = input('Включать ли символы !#$%&*+-=?@^_ ?').lower()
    while q4 not in ['да', 'нет']:
        print('Введите только да или нет')
        q4 = input('Включать ли символы !#$%&*+-=?@^_ ?').lower()
    return q4


def q5_pas():
    q5 = input('Включать ли неоднозначные символы il1Lo0O ?').lower()
    while q5 not in ['да', 'нет']:
        print('Введите только да или нет')
        q5 = input('Включать ли неоднозначные символы il1Lo0O ?').lower()
    return q5


def gen_chars():
    chars = ''
    if q1 == 'да':
        chars += digits
    if q2 == 'да':
        chars += lowercase_letters
    if q3 == 'да':
        chars += uppercase_letters
    if q4 == 'да':
        chars += punctuation
    if q5 == 'нет':
        for i in range(len(chars)):
            if chars[i] in 'il1Lo0O':
                del chars[i]
    return chars


def build_password():
    for i in range(c):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))


c = count_password()
l = len_password()
q1 = q1_pas()
q2 = q2_pas()
q3 = q3_pas()
q4 = q4_pas()
q5 = q5_pas()
chars = gen_chars()
build_password()





