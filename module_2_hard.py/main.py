import random


def random_number():
    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num1 = random.choice(list_)
    print(num1, "- случайное число")
    print()   # пустая строка
    print("набор паролей:")
    for i in range(1, num1):
        var = 0
        for j in range(1, num1):
            if num1 % (i + j) == 0 and (i < j):
                var += 1
                print(i, j, sep='', end='')


random_number()
print()     # пустая строка
