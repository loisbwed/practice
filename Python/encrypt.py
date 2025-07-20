# Вам предстоит написать программу, которая шифрует сообщения по следующему
# алгоритму: она берёт текст и переставляет в нем каждые два подряд идущих символа.

# Если количество символов нечетное, то последний символ остается на своем месте:

# encrypt("move") # 'omev'
# encrypt("attack") # 'taatkc'
# encrypt("go!") # 'og!'

# Реализуйте функцию encrypt(), который принимает на вход исходное сообщение
# и возвращает зашифрованное.

def encrypt(mord):
    list_word = []
    last_dig = []
    list_word = list(word)

    if len(word) % 2 != 0:
        last_dig = list_word.pop()
    for i in range(0, len(list_word), 2):
        list_word[i], list_word[i + 1] = list_word[i + 1], list_word[i]
    if last_dig:
        list_word.append(last_dig)
    return ''.join(list_word)

word = input('Введите слово: ')
print('Вывод: ', encrypt(word))
