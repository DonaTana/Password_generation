import random
digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^'
chars = ''

count = int(input('Введите кол-во паролей для генерации: '))
len = int(input('Введите длину одного пароля: '))
if input('Должен ли пароль содержать цифры? д-да, н-нет ') == 'д':
  chars += digits
if input('Должен ли пароль содержать прописные буквы? д-да, н-нет ') == 'д':
  chars += uppercase_letters
if input('Должен ли пароль содержать строчные буквы? д-да, н-нет ') == 'д':
  chars += lowercase_letters
if input('Должен ли пароль содержать знаки _#$%&*+-=?@^_? д-да, н-нет ') == 'д':
  chars += punctuation
if input('Должен ли пароль содержать неоднозначные символы il1Lo0O? д-да, н-нет ') == 'д':
  chars += 'il1Lo0O'

def generate_password(len, chars):
  password = ''
  for _ in range(len):
    password += random.choice(chars)
  return password 

for i in range(count):
  print(generate_password(len, chars))