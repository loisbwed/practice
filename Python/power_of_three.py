# Реализуйте функцию is_power_of_three(), которая определяет,
# является ли переданное число натуральной степенью тройки.

def is_power_of_three(num):
    for degree in range(1, 200):
        if pow(3, degree) == num:
            return True
        elif pow(3, degree) > num:
            return False

num = int(input('Ввведите число: '))
print(is_power_of_three(num))