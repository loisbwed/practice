# "Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр.
# Номера могут быть произвольной длины.

def is_happy_ticket(number):
    if len(number) % 2 == 0:
        index = len(number) // 2
        left_half = number[:index]
        right_half = number[index:]

        list_left = [int(digit) for digit in left_half]
        list_right = [int(digit) for digit in right_half]
        if sum(list_left) == sum(list_right):
            return 'Билет является "счастливым".'
        if sum(list_left) != sum(list_right):
            return 'Билет не является "счастливым".'
    if len(number) % 2 != 0:
        return 'Введите номер билета с четным количеством цифр'

number = input('Введите номер билета: ')
print(is_happy_ticket(number))