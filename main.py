# Python_2. HW_1


# 1) Создать переменную типа String
my_str='Hello Python'
print(my_str)

# 2) Создать переменную типа Integer
my_int=8
print(my_int)

# 3) Создать переменную типа Float
my_float=8.2
print(my_float)

# 4) Создать переменную типа Bytes
my_bytes=bytes([97,35,48])
print(my_bytes)

# 5) Создать переменную типа List
my_list=[my_str, my_float, 'text']
print(my_list)

# 6) Создать переменную типа Tuple
my_tuple=('Hello Python', 93,47,'text')
print(my_tuple)

# 7) Создать переменную типа
a=set('Hello Python')
print(a)

# 8. Создать переменную типа Frozen
b=frozenset('Hello Vadim')
print(b)

# 9) Создать переменную типа Dict
my_dict={"Company": "Bosch", "model": "Premio", "year":2021}
print(my_dict)

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('my_str:', my_str)
print('my_int:', my_int)
print('my_float:', my_float)
print('my_bytes:', my_bytes)
print('my_list:', my_list)
print('my_tuple:', my_tuple)
print('set:', a)
print('frozenset:', b)
print('my_dict:', my_dict)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str_1='Beautiful'
str_2='house'
str_3=str_1+str_2
print(str_3)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
str_4='Size'
int_4=2
print(str_4, int_4)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
str_5='Size'
int_5=2
print(str_5+str(int_5))
