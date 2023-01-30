import random

count = int(input('Количество паролей для генерации:'))
len = int(input('Длину паролей:'))
digit = '23456789' if input('Включать ли цифры:').lower() == 'да' else ''
big = 'ABCDEFGHIJKMNPQRSTUVWXYZ' if input('Включать ли прописные буквы:').lower() == 'да' else ''
small = 'abcdefghjklmnpqrstuvwxyz' if input('Включать ли строчные буквы').lower() == 'да' else ''
sim = '!#$%&*+-=?@^_' if input('Включать ли символы !#$%&*+-=?@^_?').lower() == 'да' else ''
minus = 'il1Lo0O' if input('Исключать ли неоднозначные символы il1Lo0O?').lower() == 'да' else ''
chars = digit + big + small + sim + minus

for _ in range(count):
    for _ in range(len):
        print(random.choice(chars), end='')
    print()