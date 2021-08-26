# class X:
#     pass

# obj  = X()
# print(dir(obj))
# print(dir(6))
# print(dir('makers'))

# 1.__init__()
# def func():
#     pass
# print(dir(func))


# class User:
#     def __init__(self,**kwargs):
#         print('Object is initializing...')
#         self.name = kwargs['name']
#         self.familia = kwargs['last_name']
#         print('Object is initialized')

# # user = User(name='Linus',last_name='Torvalds')
# # print(user.name)
# # print(user.familia)
# # 2.__new__()



# class Human:
#     def __new__(cls, *args,**kwargs):
#         print(args)
#         print(kwargs)
#         instance = super().__new__(cls)
#         instance.heart = '4csamera'
#         print('Object created')
#         return instance
#     def __init__(self,name,last_name):
#         print('Object is initializing...')
#         self.name = name
#         self.familia = last_name

# human1 = Human(name='Linux',last_name='Torvalds')
# print(human1.heart)

# human2 = Human('John','Snow')
# print(human2.heart)  



#Singleton- от одного класса можно создать только один обьект

# class Sun:
#     instance = None

#     def __new__(cls):
#         if  cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# sun3 = Sun()
# sun4 = Sun()
# # print(sun1 is sun2)
# print(id(sun1))
# print(id(sun2))
# print(id(sun3))
# print(id(sun4))

# 3.__str__()

# class Human:
#     def __init__(self,name,last_name):
#         self.last_name = last_name
#         self.name = name
    
#     def get_fullname(self):
#         return self.get_fullname()

#     def __str__(self):
#         return self.get_fullname()


# human1 =  Human('Linus','Torvals')
# # print(human1)
# print(human1)


# 4.__repr__()


# class Human:
#     def __init__(self,name,last_name):
#         self.last_name = last_name
#         self.name = name
    
#     def get_fullname(self):
#         return f'{self.name}, {self.last_name}'

#     # def __str__(self):
#     #     return f'{self.name}. {self.last_name} -срыьотал метод str'

#     def __repr__(self):
#         return f'{self.name}. {self.last_name} -срыьотал метод repr'
# human = Human('JOhn','Snow')
# print(human)


# __add__(self,other) -> +
# __sub__(self,other) -> -
# __mul__(self,other) -> *
# __truediv__(self,other) -> /
# # __mod__(self,other) -> %


# class MyInt(int):
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other):
#         self.value + other
#         return self.value + other/3

#     def __sub__(self,other):
#         print('THis is my substraction')
#         return self.value - other + 100
#     def __mul__(self,other):
#         print('This is my multiplication')
#         return self.value * other - 1
#     def __truediv__(self, other):
#         print('this is my division')
#         return self.value / other +1
#     def __mod__(self,other):
#         return f'Остаток от деления : {self.value % other}'
   
# #     """Отраженные арифметические операторы""" 
# #     #self.value + other, self.value - other
# #     #other + self.value, other - self.value
# #     def __radd__(self,other):
# #         return other + self.value

# #     def __rsub__(self,other):
# #         print('This is my r-substraction')
# #         return other - self.value 
# #     def __rmul__(self,other):
# #         print('This is my r -multiplication')
# #         return  other  * self.value + 5  
# #     def __rtruediv__(self,other):
# #         print('This is my r-division')
# #         return other / self.value - 7
# #     # """Составное присваивание"""
# #     # a = 7
# #     # a +=7  == a = a + 7
    
# #     def __iadd__(self,other):
# #         print('This is my i-addition')
# #         return self.value + other
# #     def __isub__(self,other):
# #         print('This is my-substraction')
# #         return self.value - other - 1
    
# #     def __imul__(self,other):
# #         print('This is my i-multiplication')
# #         return self.value ** other
# #     def __itruediv__(self,other):
# #         print("this is my  i-division")
# #         return self.value % other


        
        

# # # a = MyInt(10)
# # # a /= 7
# # # print(a)
# # # print( 5 + a)
# # # print(20 - a)
# # # print( a - 89)
# # # print(a + 7)
# # # print(a * 3)
# # # print(40 / a)
    

# # """"
# # __eg__ -> ==  equal
# # __ne__ -> !=  not equal
# # __gt__ -> > greater than
# # __lt__ -> <  less than
# # __le__ -> <=  less or equal
# # __ge__ -> >= greater than or equal
# # """


# # class Human:
# #     def __init__(self,name,familia,age):
# #         self.name = name
# #         self.familia = familia
# #         self.age = age
# #     def __eq__(self,other):
   
# #         return self.age == other.age
# #     def __ne__(self,other):
# #         return self.age != other.age
# #     def __gt__(self,other):
# #         return len(self.name) > len(other.name)
# #     def __lt__(self,other):
# #         return len(self.name) < len(other.name)
# #     def __ge__(self,other):
# #         return len(self.familia) >= len(other.familia)
# #     def __le__(self,other):
# #         return len(self.name) <= len(other.familia)

# # human1  = Human(name='Tom',familia="Levi",age=18)
# # human2 = Human(name='john',familia='Snow',age=34)
# # print(human1 == human2)
# # print(human1 != human2)
# # print(human1 > human2)
# # print( human1 < human2)
# # print(human1 >= human2)



# #__getattr__,__setattr__,__delattr__
# # __getattribute__

# class MyClass:
#     def __init__(self):
#         self.name = 'Makers'
#         self.last_name = 'BOOtcamp'
#         print(self.__dict__)
    
# #     def __getattr__(self,item):
# #         print(self.__dict__)
# #         return self.__dict__.get(item,'Hello world')

# #     def __getattribute__(self,item):
# #         print('This is custom getattribute magic method')
# #         return super().__getattribute__(item)
    
# #     def __setattr__(self, item,value):
# #         print(f'I want to set attribute {item} with value {value}')
# #         self.__dict__[item] = value
    
# #     def __delattr__(self, item):      #del self.item
# #         print(f'I want to delete attribute named {item}')
# #         self.__dict__.pop(item,0)

# # obj = MyClass()
# # # print(obj.age)
# # obj.age = 2
# # del obj.age
# # print(obj.age)

# # """
# # __len__(self) -> len()
# # __getitem__(self,key) -> self.key
# # __setitem__(self,key,value) -> self[key] = value
# # __delitem__(self,key) -> del self[key]
# # __contains__(self,item) -> item in self or item not in self
# # """


# # class Myclass(dict):
# #     def __getitem__(self,key):
# #         print(f'I am giving a value {key}')
# #         result = super().__getitem__(key) + 1
# #         return result
# #     def __setitem__(self,key,value):
# # #         super().__setitem__(key,value)
        
# # # dict_ = Myclass(a=6,b=7,c=8)
# # # dict_['d'] = 9
# # # print(dict_)

# class Mylist:
#     def __init__(self,iterable):
#         self.list = iterable
#     def __contains__(self,item):
#         if item in self.list:
#             True
#         else:
#             return False
# a = Mylist([1,2,3,4,5])
# print(a)


# # # # 1. Создайте класс Account и переопределите в нем методы __init__, __repr__, __str__ и __del__.
# # # # Объекты класса должны содержать атрибуты имени, баланса и города, где открыт счет.
# # # # Метод __init__ должен возвращать сообщение о создании счета, __repr__ только имя держателя счета
# # # # и баланс, а __str__ сообщение с приветствием и также информацией о держателе счета, 
# # # # балансе и филиале банка в котором зарегистрирован клиент, __del__ в свою очередь сообщение об удаление 
# # # # и слово "Пока!"
# # # # '''

# class Account:
#     def __init__(self):
#         return f'{self.count} is created!'
        
#     def __repr__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def __str__(self,name,balance,register_bank):
#         super().__str__(name,balance)
#         self.register_bank = register_bank
#     def __del__(self):
#         print('Your account has deleted , Bye')

# account = Account(name='Andrey',balance=77889,city='Bingo',)
# print(account.balance)

# # '''
# # 2. Определите класс MyNumber который наследуется от класса int. 
# # У экземпляра класса должен быть обязательный атрибут value. 
# # Переопределите методы сложения, вычитания, умножения и деления для класса таким  образом чтобы при при использовании операторов + - * / - результат возвращался с сообщением об использованном методе, 
# # например:print(num + 5)  -------> "Это сложение и Ваш результат равен 10"
# # '''

# class MyNumber(int):
#     def __init__(self,value):
#         self.value = value
#     def __add__(self,other):
#         return(f'Это сложение и Ваш результат равен {self.value + other}')
        
#     def __sub__(self,other):
#         return (f'Это вычитание и Ваш результат равен {self.value - other}')
        
#     def __mul__(self,other):
#         return(f'Это умножение и Ваш результат равен {self.value * other}')
   
#     def __truediv__(self,other):
#         return(f'Это деление и Ваш результат равен {self.value / other}')
        

# num = MyNumber(8)
# print(num * 7)
# print(num + 5)
# print(num / 2)
# print(num - 4)

# # '''
# # 3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
# # элементов начиналась с 1. Например:
# # x = MyList([1,2,3,4,5])
# # x[1] → 1
# # '''
class Mylist(list):
    def __getitem__(self,index):
        return super().__getitem__(index - 1)
new = Mylist([1, 2, 3, 4,5])
print()



    


# # '''
# # 4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
# # Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
# # '''

# """"
# 5. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
# Также в методе __new__ напишите условие для удаления
# пробелов и пустых строк в созданных словах.
# '''




# # Magic methods,dunder,super methods

# # __init__,__str__


# # __new__  #конаструктор 
# # # отвечает за создание обьекта
# # __init__ # инициалтзатор
# # # отвечает за установку свойств
# # __del__ #деструктор
# # # отвечает за удаление


# # class Course:
# #     _max_students = 10
# #     def __new__(cls,*args,**kwargs):
# #         print('New?')
# #         students = args[0]
# #         if len(students) > cls._max_students:
# #             raise Exception('.....')
# #         course = object.__new__(cls)
# #         course.__init__(*args,**kwargs)
# #         return course

# # #     def __init__(self,students:list) -> None:
# # #         self.students = students
        
# # # Если пользователь пытается добавить на курс больше максимального коичсетва студентов,то не давать создавать курс


# # # course1 = Course(['a','b','c'])
# # # course1 = Course.__new__(['a','b','c'])
# # # print(course1.students)

# # # #Single - класс, у которого может быть только 1 обьект
# # # a = 4
# # # b = 45
# # # c = 10
# # # d = None
# # # e = None
# # # f = None


# # class Contacts:
# #     _instance = None
# #     def __new__(cls,*args,**kwargs):
# #         if cls._instance is None:
# #             cls._instance = super().__new__(cls)
# #             return cls._instance
# #         raise Exception('...')
# #     def __init__(self,phone,email,address):
# #         self.phone = phone
# #         self.email = email
# #         self.address = address
# # contact1 = Contacts('789879876',
# # 'test@gmail.com','Toktogula,165')
# # contact2 = Contacts('985487548','te@gmail.com','Toktogula,165')
# # print(contact1.email)
# # print(contact1 > contact2)

# # Магические методы арифметических операций


# # '+' -> __add__(slf,other) -> self.self.other
# # a,b = 10,20
# # # a + b -> a.__add__(b)
# # class A:
# #     def __init__(self,value):
# #             self.value = value
# #     def __add__(self,other):
# #         return  self.value + other.value
# # a1  = A('67')
# # a2 = A()
# # res = a1 + a2 #-> a1.__add__(a2)
# # print(res)
# # '-' -> self - other -> self.__sub__(other)
# # '*' -> self * other -> self.__mul__(other)
# # '/' -> __truediv__
# # '//' -> __floordiv__
# # '%' -> __mod__
# # '**' -> __pow__ -> __pow__
# # 'abc()' -> __abc__

# # '+a'  __pos__
# # '-a' __neg__
# round() __round__

# # операции сравнения

# # '>' __gt__
# # '<' __lt__
# # '==' __eq__
# # '!=' __ne__
# # '>='__ge__
# # '<='__file__

# class Student:
#     def __init__(self,name,age,rating):
#         self.name = name 
#         self.age = age
#         self.rating = rating
#     def __gt__(self,other):
#         return self.rating > other.rating
# stud1 = Student('Anna',26,91)
# stud2 = Student('Aknushai',24,90)
# class int:
#     def __init__(self,value):
#         self.value = value
#     def __it__(self,other):
#         return self.value < other.value
# print(stud1 > stud2)
# print(stud1< stud2)
# преобразование типа:
# class A:
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2
#     def __str__(self):
#         return 'Value'
# a1 = A(10,20)
# # a = int('4')
# res = str(a1)
# print(res)
# str() -> __str__()
# int() -> __int__()
# float() -> __float__()
# bool() -> __bool__()


# len() __len__()
# in  __contains__()
# a = [1,2,3,4,5,6]
# a[0] #__getitem__()
# a[0] = 5 #__setitem__
# b = {'a':1,'b':2}

# b['a']
# b['a'] = 10
# del b['a']


# class A:
#     attr = 10
# a1 = A()
# a1.attr #__getattribute__()
# a1.attr = 20 #__settattr__()
# del a1.attr #__delattr__
# getattr()
# setattr()
# delattr()



import random
class Game:
    def create_coldier(self):
        for soldier in range(10):
            a = random.choice([hero1,hero2])
            print(a)
            a.new_soldier(random.randrange(20))

class Hero:

    def __init__(self,name):
        self.name = name
        self.level = 0
        self.soldier_count = []

    def  level_up(self):
        self.level += 1

    def new_soldier(self,soldier_id):
        self.soldier_count.append(soldier_id)

class Hero(Game):
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.soldier_count = []

    def level_up(self):
        self.level += 1

    def new_soldier(self, soldier_id):
        self.soldier_count.append(soldier_id)

    def __str__(self):
        return self.name


hero1 = Hero('Arstan')
hero2 = Hero('Timur')

class Soldier(Game):

    def follow_hero(self, hero):
        return f'Солдат под номером {hero2.soldier_count[2]}: иду за героем {hero}!'


game1 = Game()
game1.create_soldier()
print(hero1.soldier_count)
print(hero2.soldier_count)
print(hero1.level)
print(hero2.level)
sold1 = Soldier()
print(sold1.follow_hero(hero1))
