# # P# class Parent(object):
# #     pass
# # class Child(Parent):
# #     pass

# # # int, list, tuple,dict

# # class A:
# #     pass
# # class B(A):
# #     pass
# # class C(B):
# #     pass
# # #isinstance(obj,class)  - проверяет является ли обьект экземпляром класса
# # a = A()
# # b = B()
# # с = C()
# # print(isinstance(C, A))
# # print(isinstance(C,B))



# class Polygon:

#     sides = "many"
#     def __init__(self,*args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
       


# def get_perimeter(self):
#     if self.args:
#         return sum(self.args)
#     elif self.kwargs:
#         return sum(self.kwargs.values())
# class Rectangle(Polygon):
#     sides = 4
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

# def get_perimeter(self):
#     return self.a + self.b + self.c

# class Triangle(Polygon):
#     sides = 3
#     def __init__(self, a,b,c):
#       self.a = a
#       self.b = b
#       self.c = c

# def get_perimeter(self):
#         return self.a + self.b + self.c  
# triangle1 = Triangle(a = 2,b =4,c =7)   
# print(triangle1.sides)
# print(triangle1.get_parameter())
# class Square(Rectangle):
#     sides = 'Makers'
# square = Square(a =4)
# print(square.get_perimeter())
# print(polygon.sides)
    
# rectangle1 = Rectangle(a=7,b=7,c = 7,s=8)
# rectangle2 = Rectangle(a =9,b =7)
# print(rectangle1.sides)
# print(rectangle2.get_perimeter())

# # polygon = Polygon(8, 9,3,a= 17)
# # print(polygon.get_perimeter())

# # int,set , dict, list,bool,str
# # class MyDict(dict):
# #     def get(self,key,default='Makers'):
# #         print('This method has been changed')
# #         return dict.get(self,key,default)
# # dict1 = dict(a=7,c=7,b=9)
# # print(dict1.get('d'))

# # dict2 = MyDict(a=7,b=8,c=2)
# # print(dict2.get('d'))


# # finish
# # #Наследрвание Inheritance
# # процесс, когда один класс происходит от другого
# # #parent class ,based class
# # class A:
# #     pass
# # дочерний , производный
# # #child, inherited
# # class B(A):
# # #     pass
# # # # Дочерний класс- перенимает все атрибуты и методы родительского класса , при этои, он также может определять  свои атрибуты и методы

# # # class A:
# # #     a = 10

# # #     def method1(self):
# # #         print('Hello world')
# # # class B(A):
# # #     b = 12

# # #     def method2(self):
# # #         print('Fizz')
# # # b_obj = B()
# # # # print(b_obj.a)
# # # print(b_obj.b)
# # # b_obj.methоd1()
# # # b_obj.method2()


# # # Дочерние классы могут переопределять значения родительских атрибутов, а также переопрелеляьб поведения родительскиз методов

# # class A:
# #     a = 10
    

# # class B(A):
# #     a = 15
# # class MyClass1:
# #     def method1(self):
# #         print('hello world')


# # class MyClass2(MyClass1):
# #     def method1(self):
# #         print('Goodbye world')
# # obj1 = MyClass2()
# # obj1.method1()



# # b_obj = B()
# # b_obj.a #15
# # дочерние классы могуть не только переопредлеять методы родителя, но и дополнять их и расширять

# # super() - обращение к родителбскому классу

# # class A:
# #     def method1(self):
# #         print('Goodbye world')
# # class B(A):
# #     def method1(self):
        
# #         print('Hello world')
# #         super().method1()
      
        
# # # b1 = B()
# # # # b1.method1()

# class A:
#     attr1 = 10

#     def method1(self):
#         return self.attr1  **2

# # class B(A):
# #     b = 15
# #     def method(self):
# #         self.b = b
# #         return super().method1() 
   
# # b1 = B()
# # print(b1.method1())
        
# # Наслкдоваться можно и от встроенных классов

# # class MyString(str):
# #     def first(self):
# #         return self[0]

# #     def  last(self):
# #         return self[-1]
# # my_string = MyString('absd')
# # my_string.first() #'a'
# # my_string.last() #'d'
# # my_string.capitalize() #'ABCD'


# # a = [1,2,3,4]
# # a[0] #1
# # a[1] #1
# # # class MyList(list):
# # #     def __getitem__(self,index):
# # #         if index < 0:
# # #             super().__getitem__(index)
# # #         elif index == 0 or index > len(self):
# # #             raise IndexError('Incorrect address')
# # #         return super().__getitem__(index -1)
# # # my_list1 = MyList([1,2, 3,4])
# # # print(my_list1[-10])
# # # a = {'hey':7,'healoo':3}
# # # a.get('a') #1
# # # a.get('d') #none
# # # a.get('d',0) #0
# # # class Dict:
# # #     def get(self,key,default=None):
# # #         ...


# # class MyDict(dict):
# #     def get(self,key,default='Are you kidding'):
# #         return super().get(key,default)

# # # # my_dict1 = MyDict({'a':4,'b':3})
# # # # print(my_dict1.get('d'))

# class Human:
#     test = 'Makers'
#     def __init__(self,name,last_name,id_number):
#         self.name = name
#         self.last_name = last_name
#         self.id = id_number

#     def get_info(self):
#         super().get_info()
#         print(super().test)
#         print(f'He works as {self.position} and his salary {self.salary}')
# person = Human(name='John',last_name='snow',id_number=897)
# person.get_info()
# class Employee(Human):
#     def __init__(self,name,last_name,id_number,position,salary):
#         super().__init__(self,name,last_name,id_number)
#         self.position = position
#         self.salary = salary

#         def get_info(self):
#             super().get_info()
#             print(super().test)
#             print(f'He works as {self.position} and his salary {self.salary}')

# employee = Employee(name='John',last_name='Snow',id_number=789,position='It specialist',salary=10000)
# employee.get_info()  
# Function Super() - возвращает все методы 

# # class Animal:
# #     pass

# # class Mammals(Animal):
# #     feeding = 'Milk'

# # class Cat(Mammals):
# #     foot_count = 4
# # class HomeCat(Cat):
# #     pass
# # class WildCat(Cat):
# #     pass
# # class Tiger(WildCat):
# #     pass
# # class IndianTiger(Tiger):
# #     pass

# class A(object):
#     def method1(self):
#         print('A!')

# class B(A):
#     def method1(self):
#         print('B!')

# class C(B):
#     def method1(self):
#         print('C!')


# class D(C):
#     def method1(self):
#         print('d!')

# class E(D):
#     def method1(self):
        
#         print('E!')
# d1 = D()
# d1.method1()
# e1 = E()
# e1.method1()

#Множественное наследлвание
#MRO

# class A:
#     a = 12
# class B:
#     a = 16
# class C(A,B):
#     def get_a_(self):
#         print(self.a)

# c1 = C()
# c1.get_a_()

# """
# # 1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
# """
class Class1:
   
    def get_fruits(self):
       print('You must not eat these')
        

    def get_mandarin(self):
        print('Great choice')
class Class2(Class1):
    
    def vegetables(self):
        print('You should eat healthy food')
    def carrot(self):
          print('It is healty for teeth')
healthy_food = Class2()
healthy_food.get_fruits()
healthy_food.get_mandarin()
healthy_food.vegetables()
healthy_food.carrot()
        

        
    

     

# # """
# # 2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
# # """
# class A:

#     def __init__(self,str):
#         self.str = str(f'Main function')
        

# class B(A):

#     def method1(self):
#         super().method1('B')


# # b = B.method1('Дополнителььный функционал')
# # b.method1()

# # A.method()

# #
# # """
# # 3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
# # append, который будет принимать строку и добавлять её в конец исходной
# # pop, который удаляет из строки последний элемент и возвращает его.
# # Пример:
# # # example = MyString('String')
# # # example.append('hello')
# # # print(example) -> 'Stringhello'
# # # print(example.pop()) -> 'o'
# # # print(example) -> 'Stringhell'
# # """
# class MyString:
    
#     def append(self,add):
#         self.add = add
        
#     def pop(self,delete):
#         self.delete.pop
# class Str(MyString):

#     def __init__(self):
#         super().__init__()

# my_string = MyString()
# my_string.append('hello')
# my_string.pop([4])


        

        


    
# # # """
# # # 4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.
# # # """

# # class MyDict(dict):
# #     def get(self,key,default='Are you kidding?'):
# #         return super().get(key,default)

# # my_dict1 = MyDict({'g':8,'k':0})
# # print(my_dict1.get('m'))

# # # """
# # # 5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
# # # Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
# # # Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
# # # """
# # class Person:
# #     name = 'Sam'
# #     age = 67
# #     def display(self,name,age):
# #         self.name = name
# #         self.age = age
# #         return
# # class Student(Person):

# #     def __init__(self,name,age,faculty):
# #         super().__init__(self,name,age)
# #         self.faculty = faculty

# #     def dipslay_student(self):
# #         super().display_student()
# #         print(f'Student name: {self.name} student age: {self.age})
    
# # student_1 = 



# """
# 6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.
# """
# # писать код здесь

# Classwork
# """
# 1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
# """
# class Languages:
#   students_count = 0
#   def __init__(self):
#       self.students_count += 1
#       pass
# class Python(Languages):
#     students_count = 0
#     super().students_count =+ 1
# class JS(Languages):
#     students_count = 0
#     super().students_count =+ 1

# """
# 2) Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
# """

class PhoneBook:
  def __init__(self,name,last_name,phone_num):
    self.name = name
    self.last_name = last_name
    self.phone_num = phone_num
  def get_info(self):
    return(f'Контакт:{self.name}{self.last_name} телефон: {self.phone_num}')
call_him = PhoneBook(name='Andrey',last_name='Petrov',phone_num=997353266242)
print(call_him.get_info())