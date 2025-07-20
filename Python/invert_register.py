#Реализуйте функцию invert_case(), которая меняет в строке регистр каждой буквы на противоположный.

# invert_case('Hello, World!')  # hELLO, wORLD!
# invert_case('I love Python')  # i LOVE pYTHON

def invert_case(text):
    result = ''
    for letter in text:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result += letter.lower()
        else:
            result += letter
    return result

text = input('Введите строку: ')
print('Инверсия регистра:', invert_case(text))