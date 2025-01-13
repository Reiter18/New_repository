#5
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        return True
num = int(input('Введите число: '))
print(is_prime(num))


'''#4
def describe_person(name, age=30):
    print(f"Имя: {name}, возраст: {age}")
describe_person(input('Введите имя: '))'''


'''#3
def max_of_two(x, y):
    if x > y: return x
    return y
i, n = int(input('Введите число: ')), int(input('Введите число: '))
print('Число', max_of_two(i, n), 'большее',)'''


'''#2
def square(number):
    return number ** 2

num = int(input('Введите число: '))
print('Число', num, 'в квадрате равняется', square(num))'''


'''#1
def greet(name, msg):
    print('Привет,', name + '!', msg)
greet(input('Введите имя: '), 'Добрый день')'''