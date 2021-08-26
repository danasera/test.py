# # class, static,staticmethod,instancemethod

# # """
# # instance method -> self"
# # class method - @classmethod -> cls
# # static method  -> @ staticmethod
# # """


# class Makers:
#     language_choices = 'Python','JavaScript'


#     def __init__(self,name):
#         self.name = name

#     def instance_method(self):
#         return f'Hello {self.name}'

#     @classmethod
#     def class_method(cls):
#         return f'Welcome to Makers! What type of language do you choose?:{cls.language_choices}'

#     @staticmethod
#     def static_method(choice):
#         return f'Great! you chose {choice} course'


# student1 = Makers(name='Lucas')
# # print(student1.instance_method())
# # print(student1.class_method())
# # print(student1.static_method(choice='Pyhton'))


# # print()
# # student2 = Makers(name='Ashley')
# # print(student2.instance_method())
# # print(student2.class_method())
# # print(student2.static_method(choice='JavaScript'))


# # class User:
# #     def __init__(self,name,email):
# #         self.name = name
# #         self.email = email

# #     def get_info(self):
# # #         return f'{self.name}, {self.email}'
# # #     @classmethod
# # #     def add_data(cls,user_info:list):
# # #         name,email = user_info
# # #         return cls(name,email)


# # # list_of_users = [
# # #     ['Emily', 'emi@gmail.com'],
# # #     ['Bonny', 'boni@gmail.com'],
# # #     ['Tommy', 'tom@gmail.com']
# # # ]

# # # for info in list_of_users:
# # #     user = User.add_data(info)
# # #     print(user.get_info())

# # # user1 = User(name='Emily',email='emi@gmail.com')
# # # print(user1.get_info())


# # class Lottery:
# #     def __init__(self,name):
# #         self.name = name 

# #     @staticmethod
# #     def _generate_number():
# #         import random
# #         number = random.sample(list('123454788'),k=5)
# #         print(number)
# #         number = ''.join(number)
# #         print(number)
# #         return number


# #     def get_number(self):
# #         number = self._generate_number()
# #         self.number = number
# #         return f'Dear {self.name} ! Your lucky number is {self.number}'

# # # obj = Lottery('gigi')
# # # obj.generate_number()

# # participant1 = Lottery(name='Lucas')
# # print(participant1.get_number())


# # participant2 = Lottery(name='Nikka')
# # print(participant2.get_number())
# # print(participant2.number)



# class Pizza:

#     def __init__(self,ingredients:list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza with {self.ingredients}'

# pizza1 = Pizza(['tomatoes','mozarella','basil'])
# pizza2 = Pizza(['meat','chilli pepper','cheese'])

# print(pizza1)
# print(pizza2)

# class Pizza:

#     def __init__(self,ingredients:list):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza with {self.ingredients}'

#     @staticmethod
#     def circle_area(radius):
#         # pi * r**2
#         import math
#         area = round(math.pi * radius**2,2)
#         return f"PIzza's area is {area} sm2"


#     def area(self,radius):
#         self.radius = radius
# #         # print(self)
# #         return self.circle_area(self.radius)

# #     @classmethod
# #     def margarita(cls):
# #         return cls(['mozarella','tomatoes','basil'])

# #     @classmethod
# #     def pepperoni(cls):
# #         return cls(['peppperoni','cheese'])

# #     @classmethod
# #     def chilli(cls):
# #         return cls(['chilli','cheese','souce'])
    

    
# #   #SOLID,DRY,KISS
# # pizza1 = Pizza.margarita()
# # print(pizza1)
# # print(pizza1.area(4))
# # print('-------------------')
# # pizza2 = Pizza.pepperoni()
# # print(pizza2)
# # print(pizza2.area(8))
# # print('-------------------')
# # pizza3 = Pizza.chilli()
# # print(pizza3)
# # print(pizza3.area(5))

# # print(Pizza.margarita())
# # print(Pizza.pepperoni())
# # print(Pizza.chilli())


# # """"
# # 4. Разработчики
# # Напишите абстрактный класс Coder с атрибутом count_code_time = 0 и абстрактными методами
# # get_info и coding.
# # Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать обязательный параметр languages_backend, а Frontend — languages_frontend соответственно.

# # Переопределите в обоих классах методы get_info(Должен возвращать язык программирования и количество часов кодинга) и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time).

# # Так же бывают FullStack разработчики и
# # поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов.

# # Создайте экземпляры от классов Backend, Frontend, FullStack (obj_back, obj_front, obj_full_stack) и вызовите все их методы.
# # """

# # from abc import ABC, abstractmethod
# # class Coder:
# #     count_code_time = 0
# #     @abstractmethod
# #     def get_info(self):
# #         return

# #     @abstractmethod
# #     def coding(self):
# #         return

# # class Backend(Coder):

# #     def __init__(self,language_backend):
# #         self.backend = language_backend
    
# #     def get_info(self,time_code,language_backend):
# #         self.time = time_code
# #         self.language = language_backend
# #         return f'Language : {self.language_backend}, coding time: {self.time} '
    
# #     def coding(self,time):
# #         self.count_code_time += time
        


# # class Frontend(Coder):

# #     def __init__(self,language_frontend):
# #         self.frontend = language_frontend

# #     def get_info(self,lanaguage_frontend,time):
# #         self.frontend = lanaguage_frontend
# #         self.time = time
# #         return f'Language : {self.frontend}, coding time: {self.time} '

# #     def coding(self,time):
# #         self.count_code_time += time

# # class FullStuck(Backend,Frontend):
# #     pass

# # obj_front = Frontend('JS')
# # obj_front.coding(12)
# # print(obj_front.get_info())



# # obj_back = Backend('Python')
# # obj_back.coding(89)
# # print(obj_back.get_info())

# # obj_full_st = FullStuck('JavaScript')
# # print(obj_full_st.coding(64))
# # print(obj_full_st.get_info())





# # Given an integer n, return a string array answer (1-indexed) where:
# #     • answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# #     • answer[i] == "Fizz" if i is divisible by 3.
# #     • answer[i] == "Buzz" if i is divisible by 5.
# #     • answer[i] == i if non of the above conditions are true.
# #  
# # Example 1:
# # Input: n = 3
# # Output: ["1","2","Fizz"]
# # Example 2:
# # Input: n = 5
# # Output: ["1","2","Fizz","4","Buzz"]
# # Example 3:
# # Input: n = 15
# # Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuz


class Solution:
    def fizzBuzz(self, n: int):
        list = []
        for i in range(n):
            if i % 3 == 0 and i % 5 == 0:
                list.append
        
