# Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно.
# При этом:
    # Если число делится без остатка на 3, то вместо него выводится слово Fizz
    # Если число делится без остатка на 5, то вместо него выводится слово Buzz
    # Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
    # В остальных случаях в строку добавляется само число

# Функция принимает параметры begin и end, которые определяют начало и конец диапазона включительно.
# Функция возвращает пустую строку, если диапазон пуст — в случае, когда begin > end.

def fizz_buzz(begin, end):
    list_fb = []
    if begin > end:
        return None

    for x in range(begin, end + 1):
        if x % 3 == 0:
            list_fb.append('Fizz')
        elif x % 5 == 0:
            list_fb.append('Buzz')
        elif x % 5 == 0 and x % 3 == 0:
            list_fb.append('FizzBuzz')
        else:
            list_fb.append(x)
    return ' '.join(list_fb)

begin = int(input('Введите начальное значение: '))
end = int(input('Введите конечное значение: '))

print(fizz_buzz(begin, end))