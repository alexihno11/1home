# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# number=float(input('введите число' ))

# def summa(number):                            
#     if float(number) < 0:                            
#         x = float(number) * (-1)
#     chislo = 0

#     for i in str(number):
#         if i != '.':
#             chislo += int(i)
#     return chislo

   
# print(f'Сумма чисел равна {summa(number)}')




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('введите N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')




# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input("Введите количество чисел в списке: "))
# sum = 0
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Для n = {number}: {d}")

# def sequence(number):
#     return[round((1 + 1 / i)**i, 2) for i in range (1, number + 1)]          
# print(f'Список для {number} чисел =',sequence(number))

# for i in range(1, number + 1):
#     sum += (1 + 1 / i) ** i
# print(f'Сумма последовательности из {number} чисел равна: {sum}')



# 4.
f = open("file.txt")
a, b = f.read().split("\n")


a, b = int(a)-1, int(b)-1

N = int(input("Введите количество чисел: "))

A = []

for i in range(-N, N+1):
    A.append(i)

res = A[a] * A[b]
print(f"Position one: {a+1}\nPosition two: {b+1}\nNumber of elements: {N}\n{A}\n{res}")
