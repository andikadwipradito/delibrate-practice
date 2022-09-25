# def greet(name, name1):
#     """ fuc greet -> digunakan untuk menyapa dengan parameter 'name'
#     """
#     return name, name1


# print(greet('Melissa', 'Silvia'))

# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return "Angka minus"

# print(absolute_value(-1))

# def return_multiple():
#     return 1,2,3

# a, *b = return_multiple()
# print(f'{a=}')
# print(f'{b=}')

def my_func():
    x = 10
    return x

x = 20
print('Value outside function:' ,x)
print(my_func())