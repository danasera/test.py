# # a = 6
# # b = 7
# # print(a +b)
# # c = '7'
# # v = '8'
# # print(c + v)
# # f = [1, 2, 3, 4, 5, 6]
# # # e = [7, 8, 9,10]
# # # print(f + e)


# # # dir() - возвращает все методы класса
# # #__add__ -> +
# # a =  'Makers'
# # b = 3
# # c = [True,'bootcamp',677]
# # # d = {'MAkers':'bootcamp'}
# # # e = (6, 7, 8,9)
# f = {False,'makers',6, 7, 8}
# # # print(f"This is string methods: {dir(a)}")
# # # print(f"This is integer methods: {dir(b)}")
# # # # print(f"This is list methods: {dir(c)}")
# # # # print(f"This is dict methods: {dir(d)}")
# # # # print(f"This is tuple methods: {dir(e)}")
# print(f"This is set methods: {dir(f)}")

# # #pop() -> list, duct, set
# # list_ = [3, 4, 5, 6,7]
# # dict_ = dict(a=1,b=2, c=3)
# # set_ = {True,'Makers',78,0}

# # list_.pop(1)
# # dict_.pop('b')
# # set_.pop()
# # print(list_)
# # print(dict_)
# # print(set_)

# # update() -> dict, set
# # set_ = {True,'Makers',78,0}
# # dict_ = dict(a=1,b=2, c=3)
# # dict_.update(d =4,e=5)
# # set_.update({8,0,-1})
# # print(set_)
# # print(dict_)


# from typing import AsyncGenerator


# # class Car:
# #     def __init__(self,name):
# #         self.name = name

# #     def go_by_car(self,destination):
# #         print(f"{self.name} is going by car to {destination}")

# # class Ship:
# #     def __init__(self,name):
# #         self.name = name 
# #     def go_by_ship(self,destination):
#             # print(f"{self.name} is going by ship to {destination}")


# # class Airplane:
# #     def __init__(self,name):
# #         self.name = name
# #     def go(self,destination):
# #         print(f"{self.name} is flying by airplain to {destination}")

# # class Train:
# #     def __init__(self,name):
# #         self.name = name
    
# #     def fly_by_airplane(self,destination):
# #         print(f"{self.name}is going by train to {destination}")
# class InfoMixin:
#     def info(self):
#         my_class = self.__class__.__name__
#         print(f"I'm a {my_class} , named {self.name}, age {self.age}")
# class Cat(InfoMixin):
#     def __init__(self,name,age): 
#         self.name  = name
#         self.age = age

#     # def info(self):
#     #     print(f"I'm a Cat , named {self.name}, age {self.age}")

#     def make_sound(self):
#         print('Meow')

# class Dog(InfoMixin):
#     def __init__(self,name, age):
#         self.name = name  
#         self.age = age

#     # def info(self):
#     #     print(f"I'm a Dog , named {self.name}, age {self.age}")

#     def make_sound(self):
#         print('Woof')

# class Duck(InfoMixin):
#     def __init__(self,name, age):
#         self.name = name  
#         self.age = age

#     # def info(self):
#     #     print(f"I'm a Duck , named {self.name}, age {self.age}")

#     def make_sound(self):
#         print('Quack')

# animal = Dog('Tom',7)
# animal.info()

# # class T1:
# #     def __init__(self,iterable):
# #         self.list =  iterable

# #     def total(self):
# #         return sum(self.list)
    
# # class T2:
# #     def __init__(self,iterable):
# #         self.list = iterable
# #     def total(self):
# #         return len(self.list)

# # t1 = T1([1, 2,3 ,4,5,6])
# # t2 = T2([3, 4,5 ,6, 7,8])
# # print(t1.total())
# # print(t2.total())

# # Полиморфизм 
# """
# 1. Объявите 3 переменные, запишите в них строку, список и словарь. Затем запишите эти
# переменные в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.
# """





# str_ = 'Doncha'
# list_ = [4, 5,6 ,7,8]
# dict_ = {'Mars':9,'Bars':5}
# list1 = ['Doncha',
#        [4, 5,6 ,7,8] ,
#        {'Mars':9,'Bars':5}]
# for item in list1:
#    print(len(item))
    




# """
# 2. Создайте классы Dog и Cat с одинаковым методом voice, для собак он должен печатать "Гав", для кошек "Мяу". Создайте экземпляр от каждого класса. Затем напишите функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
# """
# # # 
# class Dog:
  
       
#     def voice(self):
#         return('GAff')
# class Cat:

        
#     def voice(self):
#         return('Meow')
    

# def to_pet(obj):
#     return obj.voice()
# animal = Dog() 
# animal2 = Cat()      
# print(to_pet(animal))
# print(to_pet(animal2))



# # # """
# # # 3. Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person.
# # # Определите во всех трёх классах метод get_info():
# # # - для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
# # # - для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
# # # - для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

# # # Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
# # # # """

# class Person:
#     def get_info(self):
#         return "Привет, меня зовут Иван Петров"

# class Employee(Person):
#     def get_info(self):
#         return "Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор\""


# class Student(Person):
#     def get_info(self):
#         return "Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе"

# person = Person()
# employee = Employee()
# student = Student()
# def get_human_info(obj):
#     return obj.get_info()
# print(get_human_info(person))
# print(get_human_info(employee))
# print(get_human_info(student))









# # """
# # 4. Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.
# # Затем наследуйте от Shape три класса: Triangle, Square и Circle.

# # - треугольник создаётся с заданными основанием и высотой
# # - квадрат создаётся с заданной длиной стороны
# # - круг создаётся с заданным радиусом

# # Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.
# # Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area().

# # # Подсказка: для создания абстрактных классов воспользуйтесь модулем [abc](https://docs.python.org/3/library/abc.html)
# # # """

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area():
#         pass

        
# class Triangle(Shape):   
#     def __init__(self,base,height):        
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height
# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
# #     def get_area(self):
# #         return self.side **2
    

# # class Circle(Shape):
# #     def __init__(self,radius):
# #         self.radius = radius

# #     def get_area(self):
# #         return 3.14 * self.radius  **2
# # square = Square(5)
# # tr1 = Triangle(10,10)
# # c1 = Circle(10)


# # print(square.get_area())
# # print(tr1.get_area())
# print(c1.get_info())

# # class House:
# #     def furniture(self,name:str,area:int):
# #         self.name = name 
# #         self.area = area
# #         print(f'{self.name}: {self.area} m2')
# #     def view_of_house(self,view):
# #         self.view = view
# #         print(f'Type of house : {self.view}')
# #     def total_square(self,area_house):
# #         self.area_house = area_house
# #         print(f'Total square : {self.area_house} m2 ')
# # sample = House()
# # # sample.view_of_house(chair,9)

# # class House:
# #     def __init__(self,type,total_area,furniture): 
# #         self.type = type
       
# #         self.total_area = total_area
# #         self.furniture = furniture
# #     def get_info(self):
# #         remaining_area = self.total_area - sum(self.furniture.values())
# #         print(self.type,self.total_area,self. furniture)
# # house = House("house",134,furniture= {'кровать': 4 , 'шкаф-купе': 2 ,
# # 'стол': 16})
# # house.get_info()

# # Полиморфизм - метод с одинаковым названием по-разному реализовывается в разных обьектах
# # a = 1
# # b = 2
# # res = a + b #3
# # res = a.__add__(b)
# # Concatenate
# # a = '1'
# # b = '2'
# # res = a + b #'12'
# # a = [1]
# b = [2]
# полиморфизм- возможность фунцции работать с обьектаит разных типов, если у них реализован опредленный метод


# len()- возвразает длину контейнера(строки списки кортежи)
# a1 = 'string'
# # a2 = [1, 2, 3,4,5]
# # a3 =  (1,2, 3,4,5 )
# # a4 = {'a':1,'b':2}

# # len(a1) #6   a1.__len__()
# # # len(a2)#5 a2.__len__()
# # # len(a3)#5 a3.__len__()
# # # len(4)#2 a4.__len__()

# # class Myclass:
# #     def __len__(self):
# #         return 0

# # obj1 = Myclass()
# # print(len(obj1))


# class Myclass:
#     def __init__(self,students):
#         self.students = students
# class1 =  Myclass(['Jaybek','Akyl','MAx','NAtalya','Ivan'])
# len(class1.students)


# def len(obj):
#     return obj.__len__()
# #List
# a1 = 1
# a2 = 2

# a3 = [1,2,3 ,4]
# class A(object):
#     pass
# a4 = A()
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(4)

# class int:
#     def __init__(self,val):
#         ...
#     def __str__(self):
#         return str(self.val)





# class Triangle:
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def triangle_area(self):
#         return 0.5 * self.base * self.height
# class Square:
#     def __init__(self,side):
#         self.side = side
#     def square_area(self):
#         return self.side **2
    
# tr1 = Triangle(10,10)
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def circle_area(self):
#         return 3.14 * self.radius  **2

#     def get_shape_area(shape):
#         if type(shape) == Square:
#             return shape.square_area()
#         elif type(shape) == Circle:
#             return shape.circle_area()
#         return shape.triangle_area()
# c1 = Circle(10)
# # print(get_shape_area(tr1))



# Abstract Class - класс , который имеет абстрактный метод(класс , который нужно уточнить при насоедовании)

# class Transport:
#     def  move(self):
#         raise NotImplementedError()
# class LandTransport(Transport):
#     def move(self):
#         print('Двиается по суше')


# tr1 = LandTransport()
# tr1.move()

from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        print('Fly')
class AirTransport(Transport):
    pass
    # def move(self):
    #     print('Fly')
obj1 = AirTransport() #Error
