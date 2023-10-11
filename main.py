# < Іваньо Іван >
# Лабораторна робота № 3.4
# Розгалуження, задане плоскою фігурою.
# Варіант 0.6

x = int(input())
y = int(input())
R = int(input())

if ((x ** 2 + y ** 2 <= R ** 2) and y >= 0) or ((x ** 2 + y ** 2 >= R ** 2) and y < 0):
    print('YES')
else:
    print('NO')
