# # # def  sum(func):
# # #     def wrapper(*args,**kwargs):
# # #         return kwargs.get('b')
# # #     return wrapper
# # # # @sum
# # # # def take(*args,**kwargs):
# # # #     return 
# # # # print(take(4, 5,7,8,a='hello',b='baby'))


# # # # users = {
# # # a = [3, 4,5,6]
# # # def sum (*args):
# # #     from functools import reduce
# # #     x = list(reduce(lambda x, y: x + y,a))
    

# # # class A:
# # #     pass
# # # class B(A):
# # #     pass
# # # class C(B):
# # #     pass
# # # print(C.mro())

# # def  bold_(func):
# #     def wrapper():
# #         return f'<b>{func()}</b>'
# #     return wrapper

# # def in_(func):
# # #     def wrapper():
# # #         return f'<i>{func()}</i>'
# # #     return wrapper

# # # def un_(func):
# # #     def wrapper():
# # #         return f'<u>{func()}</u>'
# # #     return wrapper
# # # @bold_
# # # @in_
# # # @un_
# # # def word():
# # #     return 'Hello world!'
# # # print(word())

# # class Circle:
# #     circle_color = 'blue'
# #     pi = 3.14
# #     def __init__(self,radius):
# #         self.radius = radius 
            

# #     def formula(self):
# #         return f'rezultat : {self.pi * self.radius **2}'

# # result = Circle(5)
# # print(result.formula())


# class Song:
#     def __init__(self,title,author,date):
#         self.title = title
#         self.author = author
#         self.date = date
#     def show_author(self):
#         return f'Author - {self.author}'

#     def show_title(self):
#         return f'Title - {self.title}'

#     def show_year(self):
#         return f'This song was released {self.date}'
# my_song = Song(author='Mozart',title='Seasons',date=1992)
# print(my_song.show_author())
# print(my_song.show_title())
# # print(my_song.show_year())

# class A:
#     def method1(self):
#         print(' Main function')
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Added function')

# result = B()
# result.method1()

# def move(self):
#     pass
# a = 1

# def func1():
#     pass
# class A:
#     pass

# from example.test1 import *

# a = 10
# print(a)  

# -*- coding: utf-8 -*-
        


