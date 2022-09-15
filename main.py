import math
from random import randint
import sympy as sp

# Вычислить число c заданной точностью d
num = float(input("Введите вещественное число: "))
d = len(input("Задайте точность числа: ").split(".")[1])
print(f'Число при заданной точности: %.{d}f'%num)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите N: "))
prime_list = [i for i in range(2, int(math.sqrt(n)) + 1) if sp.isprime(i) and n % i == 0]
print(prime_list)

# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
num_list = "2 3 33 2 435 24 3 1 242 -32"
print(set(num_list.split(" ")))

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
k = int(input("Введиде K: "))
x = sp.Symbol('x')
res = ""
for i in range(k, -1, -1):
    res += f"{randint(0,100)*x**i}" 
    if i > 0:
        res += "+"
with open("text.txt", "w") as f:
    f.write(str(sp.simplify(res)))

# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
with open("text.txt", "r") as f, open("text2.txt", "r") as f2, open("res.txt", "w") as r:
    r.write(str(sp.simplify(f.read() +"+"+ f2.read())))

