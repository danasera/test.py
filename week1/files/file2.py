


#Файлы

# Операции над файлами:
# 1. read
# 2. запись
# файлы бывают текстовые и бинарные
# open() - фунция для открытия файла
# open(road to the file,режим)
# open('test.txt')
# open('/home/adilet/python13/week4/test.txt')
# open('~/python13/week4/test.txt')

# 'r'(read) чтение 
# 'w'(write) перезапись
# 'x'(exclusive) запись в новый файл
# 'a'(append) длзапись
# '+' чтение и запись
# 't'- текстковый
# 'b'- бинарный


# Read  
# read()- считывакт содержимое всего фвйла в виде одной большрй строки
# readlines()- считывает все содержимое файла в виде списка строк
# readline()- сяитывает каждый раз по одной строке

# from typing import ClassVar


# f = open('test.txt','rt')
# content = f.readline()
# print(content)
# print(type(content))

# f = open('test.txt','r')
# content = f.read()
# f.seek(0)
# content2 = f.read()
# print(content2)

# #Запись
# 'w' - удаляет содержимое,  и поверх записывает новое
# 'x'- еу записывает существующий файл
# 'a'- дозаписывает

# write(str) - зписывает по однрй строке
# writelines(list) - записывает список из строк
# f = open('test.txt', 'w')
# f.write('if number >  20: \n')
# f.write('Hello World\n')
# f.write('Monty Python\n')

# f.write("\tprint("hello world")


# f.write(["if number > 20: \n", "\tprint('something')"]
# f.close()


# f = open('test.txt')
# for lines in f:
#     print(line)

# f = open('test.txt', 'wt')
# # f.write('Hello world\n')
# # f.write('monty python\n')
# # f.seek(0)
# # content = f.read()
# # print(content)
# # f.close()

# json, csv -формат (структурированные данные)
# формат - передача данных
# JSON(Javascript object Notation)

# import json 


# human = {
#     'name': 'Ivan',
#     'last name': 'Petrov',
#     'age':26,
#     'hobbies':['swimming', 'dancing'],
#     'is_married': False,
#     'driving_licence': None
# }
# human = '{"name": "Ivan","last_name": "Tetpov","age":25,"hobbies": ["swimming", "footaball"], "is_married":false, "driving_licence": null}'

# # json_str = json.dumps(human)
# print(json_str)

# import json 
# json_str = json.dumps(human)
# print(json_str)

# dumps(python_object)- переводит python obj в json строку

# # loads(json_str)- переводиит json строку в python obj

# people_json  = '[{"name": "Vadim", "last_name":"Rebrov"},{"name":"Max","aleksey":"curator"," ":"null"}]'
# people = json.loads(people_json)
# print(people[0]['name'])

# dump() - запись python обьуктов в json файл
# load() - чтение обьектов из json файлв
# f = open('products.json','r')
# content = f.read()
# products = json.loads(content)

# # f = open('products.json','r')
# products = json.load(f)

# в json:
# ключом может быть строка 
# кавычки должны быть двойными



# company = {'name': 'McDonald\'s','address':'Washington'}
# res = json.dumps(company)
# print(res)

# Python        JS
# int, float    number
# str           string
# list, tuple   array
# dict          object
# True/False    true/False
# None          Null
# products = [
#     {
#      'title': 'Apple Iphone 12',
#      'price': 10000
#     },
#     {
#      'title':'Xiomi Mi 11',
#      'price': 50000
#     },
#     {
#      'title':'sumsumg S21',
#      'price': 65000
#     }
# ]

# import json
# f = open('products.json','w')
# # products = json.dumps(products)
# json.dump(products, f)
# f.close()
# CSV(Comma-separated value)
# , ФИО, Дата рождения, Адрес
# 1, Иманбеков Айбек Максатович, 28.09.2002, ул.Токтогула, 187
# 2, Уланьекова Гульзада Тилековнаб, 20.09.2001, ул.Токтогула, 187
# import csv

# запись
# with open ('students.csv','w') as f:
#     stud_writer = csv.writer(f)
#     stud_writer.writerow(['#','ФИО', 'Дата рожления', 'Address'])
#     stud_writer.writerow(['1','Akylbekova aidai MAratovna','23.09.1993','street Toktogula'])

# чтение
# with open('students.csv','r') as file:
#     csv_reader = csv.reader(file, delimiter = ',')
#     for row in csv_reader:
#         print(row)
# with open ('students.csv','r')

# with open ('students.csv', 'w') as file:
#     csv_writer = csv.DictWriter(file,['#','фио','Date of Birth','address'])
#     csv_writer.writeheader()
#     csv_writer.writerow({'#': 1, 'фио':'Akylbekova aidai Maratovna','Date of Birth': '20.09.1995','address': 'st. Kiev, 5'})

#file1 = open('makers2.txt','r')
# print(file1.read())

# r - read
# r+ -read + write 
# w - write 
# w+ - read + write 
# a - append
# a+ append + read 
# x - write 
# b - binary 
# t - text 
# rt -> r 
# rb -> rb 
# file1 = open('makers.txt', 'r')
# data = file1.read(3)
# print(data)
# print(file1.read(10))
# print(file1.read(10))
# file1.seek(3)
# print(file1.read(10))
# file1.seek(3)
# print(file1.read(5))

# print(file1.read(10))
# print(file1.read())
# print(file1.read(6))


# seek 
# file1 = open('makers.txt', 'r')

# print(file1.readline())
# print(file1.readline())
# print(file1.readline())
# for line in file1:
#     print(line)
# list_ = file1.readlines()
# print(list_)
# list_ = file1.readline()
# list_ = [line.replace('\n','') for line in list_]
# print(list_)

# file2 = open('bootcamp.txt', 'w')
# # file2.write("It is such a beautiful name" + '\n')
# # file2.write("Today is my birthday" + '\n')

# list_of_books = ["Автостопом по галактике","Aнна Каренина",
#                   "Американский психопат","Алиса в Стране чудес"]
# list_of_books = [motto + '\n' for motto in list_of_books]
# print(list_of_books)
# file2.writelines(list_of_books)

# dict_ = {'name': 'Makers','hello':'world'}
# file2.writelines(dict_)

# file2 = open('bootcamp.txt', 'w')
# list_of_books = ["Автостопом по галактике","Aнна Каренина",
#                   "Американский психопат","Алиса в Стране чудес"]
# # list_of_books = [motto + '\n' for motto in list_of_books]

# file2.write('Mottos of big companies')
# for motto in list_of_books:
#     file2.write(motto)
# file3.close()
# print(file3.closed)
# with - оператор, который автоматически закрывает файл по окончании работы с ним(инструмент упрощает чтение и редактирование файлов) 

# with open('files.txt','w+') as my_file:
#    print(my_file.read())
#    my_file.write('ADditional stirng')
#    my_file.write('Hello world!')
#    print(my_file.close)

# math, random, datetime
# import math

# math, random, datetime
# import square
# from square import circle, triangle, rectangle



# with open('task1.txt', 'w') as file:
#     for number in range(1,11):
#       file.write(str(number) + '\n')
# print(file)
# res = 1
# spl = list(map(int, spl))
# print(spl)

# with open('ta')
# with open('task1.txt', 'w') as file:
#     for number in range(1,11):
#       file.write(int(number) + '\n')
#       file.read(5)
# print(file)
with open('')
