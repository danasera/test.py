# class SomeClass:
#     pass
# class A:
#     pass
# a = A() - # экземрляр  класса , обьект класса, instance, object
# print(isinstance(a, A))
# a = 4
# print(type(a))
# # свойства
# class str:
#     #свойства
#     pass
# class list:
#     pass
#     #свойства
# # class B:
# #     pass
# # int,str, tuple,dict,set,bool, set, frozenset
# # a = 5
# # print(type(a))
# # v = 'string'
# # print(type(v))
# # c = [4, 5,6 ,7]
# # print(type(c))

# class Dog:
#     owner = 'John'
    

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'{self.name}, {self.age}'
#     def bark(self):
#         print("GAv-Gav")
#     def dog_info(self):
#         return f'This is {self.name}, he is {self.age} years old'
#     def birthday(self,cake):
#         self.age +=1
#         self.cake = cake
#         return f' {self.name} is {self.age} y.o now'
        
#     def eat(cls):
#      print('Yummy')
#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self

# dog1 = Dog(name = 'Rex',age = 3)
# dog2 = Dog(name = 'bobik',age = 6)
# dog3 = Dog(name = 'Oreo',age = 8)
# dog1.friends(dog2)
# print(dog1.friend.name)
# print(dog2.friend.age)
# # dog1.birthday()
# print(dog1.birthday('strawberry'))
# print(dog2.birthday('vanilla'))
# print(dog3.birthday('chocolate'))
# print(dog1.cake)
# print(dog2.cake)
# print(dog3.cake)


# dog1.bark)
# dog2.bark()
# dog3.bark()

# dog3.owner = 'Alice'
# # print(dog1.name)
# # dog1.name = 'Mike'
# # dog1.food = 'meat'
# # print(dog1.food)
# # print(dog2.food)
# # print(dog2.name)
# # print(dog1.owner)
# # print(dog2.owner)
# # print(dog3.owner)
# # print(dog3.name)



# #Rectangle
# class Rectangle:
#     default_color = 'red'

#     def __init__(self, width,lenght):
#         self.width = width
#         self.length = lenght
#     def area(self):
#         return self.width * self.length

# rec1 = Rectangle(4,5)
# rec2 = Rectangle(4,7) 
# rec2.default_color = 'pink'
# print(rec1.area())
# print(rec1.width)
# print(rec2.area())
# print(rec1.default_color)
# print(rec2.default_color)


# class Car:
#     car_count = 0

#     def __init__(self):
#         Car.car_count +=1
# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.car_count)

# Наследование
# Abstraction
#Композиция
# Инкапсуляция
#полиморфизм


# # OOP (обьекно ориентированнное программирования)
# # a = 4
# # b = '5' #string
# # c = [1, 2, 3] # list
# # d = {1, 2, 3, 4}  #set

# # class MyClass:
# #     a = 10 - #atribute

# #     def method1()

# # a = 'string'
# # a.capitalize()

# # class str:
# #     def capitalize(self):
# #         pass

# # Класс- способ описания обьектов , какие характеристики у обьекта(атрибуты), какие дейсвия он может выпрлнять (method)
# # class Student:
# #     course = 5  #atribute of class

# #     def __init__(self,last_name,age,name):
# #         #   атрибуты экземпляра
# #         self.first_name = name
# #         self.last_name = last_name
# #         self.age = age
# #     def get_profile(self):
# #         #Madina Alieva,21,3 course
# #         return f'{self.first_name}{self.last_name}{self.age} y.o {self.course} course'


# #     # name = 'tilek'
# #     # last_name = 'Sagynbekov'
# #     # age = 25

# #     def sleep(self):
# #         print('Sleep during studing')

# # student1 = Student('Bas','Nakipan',34)
# # student2 = Student('Aidan','makirova',98)
# # student3 = Student(name='Bakyt',last_name='Napkin',age = 87)
# # print(student2.get_profile())
# # student2.first_name
# # Student.get_profile(student2)
# # student2.__getattribute__('get_profile')

# class Patient:
#     def __init__(self,name,last_name,weight, height):
#         pass
# class Client:
#     def __init__(self,name, last_name,dat_of_birth,passport):
#         pass

# # class Customer:
# #     def __init__(self,name,age,phone_number):
# #         pass
# # #принцип абстрагирования  read about this
# # class Notebook:
# #     def __init__(self,color,diagonal, cpu,ram,hdd):
# #         pass
# # class Notebook:
# #     def __init__(self,bran,model,color, diagonal,characteristics,price):
# #         pass
# class Engine:
#     def __init__(self,fuel,volume,power):
#         self.fuel = fuel
#         self.volume = volume
#         self.power = power
# engine1 = Engine('diesel',3.5,'power')
# class Car:
#     brand = 'Hyundai'

#     def __init__(self,model,color,volume,engine,interior,price):
#         self.model = model
#         self.color = color
        
#         self.engine  = engine
#         self.interior = interior
#         self.price = price

# car1 = Car('Genesis','Black',3.0,engine1,'leather',78)


class Product:
    '''Класс , описывающий продуктыю
    Принимает назвние продукта и цену'''
    def __init__(self,price):
        self.title = title
        self.price = price
    def __str__(self):
        return self.title
help(list)
        
# product1 = Product(title='Apple Iphone 12',price = 1000000)
# product2 = Product(title = 'Apple MacBook pro',price = 64734)
# product3 = Product(title = 'Samsung GAlaxy s21',price= 77890)
        
# class User:
#     def __init__(self, email, password,name, address):
#         self.email = email
#         self.password = password
#         self.name = name
#         self.address = address


        
# user1 = User('test2@gmail.com',password= 'qwery',name = 'Nurbek',address = 'st.Toktogula,176')    
# class Order:
#       def __init__(self,user,items):
#           self.user = user
#           self.items = items
# order1  = Order(user1, [{'product':product1,'quantity':1},{'product':product2,'quantity':34}])
# order1.user.address
# # class int:
#     def __init__(self) -> None:
#         pass
# # a = int(x=23)
# # def __str__(self): - описание обьекта
#     return str(self.x)
# a = 23 - get number
# print(user1)
# print(product2)
# print(product3)
# """
# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
# """
# class Circle:
#   default_color = blue
#   pi = 3.14
#     def __init__(self,radius):
#     self.radius = radius
#     self.
#        def calc()
# """
# 2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
# """
# # писать код здесь
# """
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
# """
# # писать код здесь
# """
# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """
# # писать код здесь
# """
# 5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
# """
# # писать код здесь



class A(object):
    pass
a1 = A()
print(dir(a1))
        