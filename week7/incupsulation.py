# # # Модификаторы доступа:
# # 1. public- password, get_info
# # # 2. protected -  _password,_get_info()
# # # 3. private - __password,__get_info()
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#     def get_password(self,username):
#         if self.username == username:
#             return self.__password
#         else:
#             return 'No!'
#     def set_password(self,old_password,new_password):
#         self.__password = old_password
#         self.__password = new_password
#     def get_info(self):
#         print(f"Username {self.username}, password {self.password}")
# user1 = User(username='makers123',password='bootcamp789')

# print(user1.username())
# print(user1.get_password(username='makers123'))
# user1.set_password(old_password='bootcamp789',new_password='helloworld45')
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username= 'makers123'))

# class Divider:
#     def __init__(self):
#         self.__divide_num = 2
#         # self.divide_num = 0
#     @property   #-> getter
#     def get_divider(self):
#         return self.__divide_num
    # @divider.setter #-> setter 
#     def divider(self,value):
#         if not value == 0:
#             self.__divide_num == value
#             return "Successully changed divide number"
#         else:
#             return "Error"
# #     def divide(self,value):
# #         return value / self.__divide_num
# # obj = Divider()
# # # # obj.__divide_num = 0
# # # # print(obj.get_divider())
# # # print(obj.divider)
# # # print(obj.divide(7))
# # # obj.divider = 14
# # # print(obj.divider)

# # # class Person:
# # #     def __init__(self,name,last_name):
# # #         self.name = name
# # #         self.last_name = last_name
# # #     def full_name(self):
# # #         return f"{self.name} ,{self.last_name}"
# # # person = Person(name='John',last_name='Snow')

# # # print(person.full_name())

# # class Car:
# #     def _inject_fuel(self):
# #         print('Fuel injected')
# #     def _init_bang(self):
# #         print('Bang!')
# #     def _send_signal_to_ignition_system(self):
# #         print("ignition started")
# #         self._inject_fuel()
# #         self._init_bang()
# #     def _send_signal_to_pc(self):
# #         print('Start')
# #         self._send_signal_to_ignition_system()
    
# #     def start_engine(self):
# #         self._send_signal_to_pc()
# # car = Car()
# # car.start_engine()    
# # car._init_bang()


# # 1. underscore
# # 2.protected - мы еще можем получить скрытые данные
# # 3.protected данные наследуются в дочерних классах

# # class A:
# #     def __say_hello(self):
# #         print('Hello, makers!')
# # class B(A):
# #     pass
# # b = B()
# # # b.__say_hello()
# # """"
# # # 1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
# # # """
# # class Methods:
    
# #     def public_method(self):
# #        pass
# #     def _protected_method(self):
# #         pass
# #     def __private_method(self):
# #         pass
# # methods = Methods()
# # methods.public_method()
# # methods._protected_method()
# # methods._Methods__private_method()

# # """
# # 2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". Затем создайте класс B, который будет наследоваться от класса A. Создайте экземпляр от класса B, и через него вызовите метод method1.
# # """
# # class A:
# #     def method1(self):
# #         print('Hello world!')
# # class B(A):
# #     def method1(self):
# #         pass
# # method = B()
# # method.method1()

# # """
# # 3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. Затем определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, с помощью которого Вы будете получать значение скорости.
# # """
# class Car:
#     __speed = 30
    
#     def set_speed(self,speed):
#         self.speed = speed
  
#     def show_speed(self):
#         print(self.speed)
# car = Car()
# car.set_speed(15)
# car.show_speed()
    

# # """
# # 4)Перепишите класс Car из предыдущего задания.
# # Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property, для того чтобы можно было работать с данным классом следующим образом:

# # car = Car()
# # car.speed = 120
# # print(car.speed)
# # """
# class Car:
#     __speed = 0
#     @property
#     def speed(self):
# #         return self.__speed

# #     @speed.setter
# #     def speed(self,new_speed):
# #         self.speed = new_speed
 
# # car = Car()
# # car.speed = 120
# # print(car.speed)



# # # #Encupsulation
# # # 1.Обьеденение данных и фунции , крирпрые работают с этими данными в один обьект
# # # 2.Набор инструментов для сокрятия реализации оббьекта

# # # Modificators Модификаторы доступа:
# # # public -
# # # Публичные атркбитуты и методы доступны в классе,  в дочерних классах и вне класса
# # class A:
# #     attr1 = 10  #public
# #     _attr2 = 12 #protected
# #     __attr3 = 15 #private
# #     def method1(self): #public
# #         pass
# # class B(A):
# #     pass
# # b1 = B()
# # print(b1._attr2)
# # b1._attr2 = 20
# # print(b1._attr2)



# # print(b1.__attr3)
# # b1._A__attr3
# # # protected -защищенные атрибуты и методы недоступны вне класса, но при этои длступны в самом классеи его дочерних класса
# # # private- приватные атрибуты и иетоды длступны только внутри класса, где они определены, и недоступны в дочерних классах и вне классаю

# # class A:
# #     def __init__(self,value):
# #         self.__attr1 = value
# #     #setter
# #     def  set_attr1(self,new_value):
# #         self.__attr1 = new_value
# #     #getter
# #     def get_attr1(self):
# #         return self.__attr1
# # a1 = A(4)
# # a1.set_attr1(20)
# # a1.get_attr1()
# # class Car:
# #     __speed = 0
# #     @property
# #     def speed(self):
# #         return self.__speed
# #     @speed.setter
# #     def speed(self,new_speed):
# #         self.__speed = new_speed
# # car = Car()

# # car.speed = 20
# # print(car.speed)

# from functools import reduce
# class ToDoList:
#     def __init__(self):
#         self.list_ = []
#     def put(self,to_do):
#         self.list_.append(to_do)
#     def get(self):
#         print(self.list_)
#         get = [[i.task,i.priority]for i  in self.list_]
#         print(get)
#         if get:
#             max_value = [reduce(lambda x,y:x if y[1] > x[1] else y,get)]
#             return max_value
#         else:
#             return None
#     def count(self,priority=1):
#         self.priority = priority
#         self.counts = []
#         for i in self.list_:
#             if self.priority in range(1,6):
#                 if i.priority == self.priority:
#                     self.counts.append(i)
#                     print(i)
#             else:
#                 self.priority = 0
#         return f'{(len(self.counts))}'
        



# class Task: 
    
#     def __init__(self,task,priority=3):
#         self.task = task
#         self.priority = priority

#     def __str__(self):
#         return f' {self.task}{self.priority}'
# test = ToDoList()
# # a = Task('read book',6)
# # b = Task('help grandmother',3)  
# # s = Task('buy ginger',7)     
# # test.put(a)
# # test.put(b)
# # test.put(s)
# # print(test.get())
# # print(test.count())
# # print(test.count(3))

# class MobilePhone:
   
#     __battery = 100
#     def __init__(self, info):
       
#         self.info = info
    


#     def music(self):
#         if self.__battery <= 0:
#             raise 'Phone is dead'
#         self.__battery -= 5.5
        

#     def video(self):
#         if self.__battery == 0:
#             raise 'Phone is dead'
#         if self.__battery >= 10:
#             self.__battery -= 7.5
#         else:
#             print('Your phone is unavailable!')
#     def charge___battery(self,time):
# #         self.time = time 
# #         self.__battery += self.time *10
# #         if self.__battery > 100:
# #             self.__battery = 100
# # a = MobilePhone('info')
# # a.music()
# # a.video()

# # # a.charge___battery(2)
# # print(a._MobilePhone__battery)

# class Tomato:
#     states = {0:'seed',1:'flower',2:'green',3:'red'}
#     def __init__(self,index):
#         self._index = index
#         self._state = 0
       
        
        
#     def grow(self):
#         self._change_state()
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         else:
#             return False
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#     def _print_state(self):
#         print(f'Tomato {self._index} is {self._state}')
# class TomatoBush:
#     def __init__(self,num):
#         self.tomatoes = [Tomato(index) for index in range(0,num +1)]
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#     def all_are_ripe(self):
#             return all([tomato.is_ripe() for tomato in self.tomatoes])
#     def give_away_all(self):
#         self.tomatoes == []
# class Gardener:
#     def __init__(self,name,plant):
# #         self.name = name
# #         self._plant = plant
# #     def work(self):
# #         print('GArdener is working')
# #         self._plant.grow_all()
# #         print('GArdener has finished work')
# #     def harvest(self):
# #         if self._plant.all_are_ripe() == True:
# #             self._plant.give_away_all()
# #             print('Harvesting is over')
# #         else:
# #             print('It is too early to harvest') 

# #     def knowledge_base(self):
# #         print('Tomatoes should be grabbed')

# # tomato_bush = TomatoBush(4)
# # work2 = Gardener('Jupiter',tomato_bush)
# # work2.knowledge_base()
# # work2.work()
# # work2.harvest()

# class Parent:
#     x = 1
#     y = 2
# class Child(Parent):
#     x = 111
#     y = 222
#     def mix(self):
#         return Parent.y
# a = Child()
# print(a.mix())



"""Напишите декоратор repeat, который принимает как именованный аргумент num целое число (количество выполнения декорированной функции) и запускает декорированную функции указанное количество раз.

Например
```python
@repeat(num=4)
def function(name):
    print(f"{name}")

При вызове function("Python"), вывод должен выглядеть так:
Python
Python
Python
Python
"""

def repeat(num=1):
    def momo(func):
        def wrapper(*args,**kwargs):
            n = num
            for i in range(num):
                print(n)
                n -= 1
            func(*args)
        return wrapper    
    return momo


@repeat(num=8)
def function(name):
    print(f'{name}')
function("python")


"""Напишите декоратор countdown, который принимает параметр seconds и отсчитывает секунды до запуска декорированной функции.

Например:
```python
@countdown(seconds=5)
def func():
    print('Hello world')
```
#вывод
5
4
3
2
1
Hello world!
"""

# писать код здесь





    
           