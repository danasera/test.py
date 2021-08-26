# условные и логические операции

# сравнения
# "==" - равенство
# "!+" - неравенство
# "<>" - неравенство
# "<" - меньше
# ">" - больше
# "<=" - меньше или равно
# ".=" - больше или равно

# x = 1-
# y = 15

# x > y  False
# x < y  True
# x != y True 

# x = '10'
# y = 9

# (x) > y - Error

# x = 'a'
# y = 'b'
# x > y Falsse

# '' < '+' True
# '+' < '0' True
# '0' < 'a' True
# 'A' < 'a' True
# 'z' < '{' True
# '{' < '~' True 

# 'Ann' < 'Annabel'
# 'abc' < 'abd'


# проверка
# in - проверка на вхождение
# is - является  ли
# isinstance(щбъект, class) - проверятьб относится ли обьект к определенному классу
# issubclass(лкасс1 класс2)-  проверяет, является ли класс1 потомкщм класса2

# isdigit(), islowwer(), isdecimal() check something


# приведение в bool

# bool(0)  False
# bool(none)  False
# bool('') - False
# bool([])) - False
# bool(()) -False
# bool({}) - False
# bool(set()) - False

# bool(-1) - True
# bool(10) - True
# bool('')- True
# bool([1,2]) - True
# ...

# if условие:
# # action    
# number = 20

# if number > 15:
#     print('Hello world')

#     a = 'My string'

# if 'e' in a:
#     print('Yes')

# b = 'Hello world'
# if b.isalpha():
#     c = 'good'

#     a1 = [ 1, 2, 3, 4]
#     if len(a1) > 0:
#         print('Ok')

#     if bool(a1):
#        print('Ok')

#     if al:
#         print('Ok')
#         ort_mark = 195
#          if ort-mark < 105:
#              print('Bad')
#     else:
#         print('{Good') 

# temperature = 40 

# if temperature < 19:
#     print('Cold')
# else:
#     if temperature < 28:
#         print('Warm')  
#     if: temperature < 35:
#         print ('Hot')
#     else:
#         print('Too hot')
#  if temperature < 188:
#      print('cold')
#  elif temperature < 28:
#      print('Warm')
#  elif temperature  < 35:
#      print('Hot')
#  else:
    #  print('Too Hot') 


#  If temperature < 18:
#        ...
#  If temperature < 28:
#     ...
#     if temperature  >= 28 and temperature < 35:
#  mark = int(input('Введите оценку щт 1 до 100: '))   
# 
# 0 - 60 -> 2
# 61- 75 -> 3
# 76 - 84 -> 4 
# 85 - 100 -> 5
#  
# if mark < 61:
#  result = 2
# elif mark < = 75
#  result = 3
# elif mark <= 84
# result = 4
# else:
#      result = 5
# print(result)     
# x = 20 

# while True:
#     number = int(input('Введите число'))
#     if x == number:
#         print('Выигрыш!')
#         break
# print('Try again!') 
#  logic operator
#  and
#  or
#  not   

# #  False and False - False  
# True and False - False
# False and True - False 
# True and True - True

# False or False - False
# True or False - True
# False or True -True
# True or True - True


# not True -False
# not False - True

# temperature = 100
# pressure = 5

# if temperature > 120 and pressure
# > 3:
#    print('reaction work')
#     time = 16

# if time < 15 or time > 18:
#     print('Work time')

# has_car = False

# if not has_car:
#     print('you can not go')




    
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: ')) 
choice = input('Выберите - % / *: ')

# dict_ = {
#     '+': first_number + second_number
#     '-': first_number - second_number  
#     '*': first_number * second_number 
#     '/': first_number / second_number 
#     '%': first_number % second_number 
# }
#  print(dict_,get(choice))10


if choice == '/' and second_number == 0:
    print('Целое число нельзя делить на 0')  
    
if choice == '+':
        print(first_number + second_number)
elif choice == '-':
    print(first_number - second_number)
elif choice  == '*' :
    
elif choice  == '/' :
    print(first_number / second_number)    





     



