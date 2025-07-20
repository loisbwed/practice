# Реализуйте функцию is_perfect(), которая принимает число и возвращает True, если оно совершенное, и False — в ином случае.
# Совершенное число — это положительное целое число, равное сумме его положительных делителей (не считая само число).

num = int(input('Введите число: '))

def perfect_num(num):
    div = 1
    list_div = []
    while div < num:
        div += 1
        if num / div == round(num / div):
            list_div.append(int(num / div))

    if sum(list_div) == num:
        return 'Данное число является "идеальным"'
    else:
        return 'Данное число является не "идеальным"'

print(perfect_num(num))