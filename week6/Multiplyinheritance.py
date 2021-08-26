


# class Parent:
#     def who_am_i(self):
#         print("I am  a parent")
# class Child(Parent):
#     def who_am_i(self):
#         super().who_am_i()
#         print("I am a child")
# child = Child()
# child.who_am_i()


# # Множественное наследование
# class Grandpa:
#     # pass
#     def talant(self):
#         print('I am good at dancing')
# class Grandma:
#     # pass
#     def  talant(self):
#         print('I am good at drawing')


# class Father:
#     last_name = 'White'
#     # pass
#     def talant(self):
#         print('I am good at swimming')
# class Mother(Grandpa,Grandma):
#     last_name = 'Brown'
#     def talant(self):
#         print('I am good at cooking')
# class Child(Mother,Father):
#     pass
# child = Child()
# print(child.last_name)
# child.talant()
# print(Child.mro())

# class A:
#     def __init__(self,param):
# #         print(f'Hey,It is A class, I got {param} parameters')
# #     def get_letter(self):
# #         print("AA")
# # class B:
# #     def __init__(self,param):
# #         print(f'Hey,It is B class, I got {param} parameter')
# #     # def get_letter(self):
# #     #         print('BBB')
# # class C(A,B):
# #     pass
#     # def get_letter(self):
#     #     print('CC')
#     # def __init__(self):
#     #     print(f'Hey, It is C class , I do not get any parameter')
# # c = C('MAkers')
# # print(C.mro())
# # c.get_letter()
# # c.get_b()
# # c.get_c()

#         #     A
#         #   /   \
#         #  B --- C
#         #   \   /
#             # D


# class A:
#     def method(self):
#         print('Hello,I am A')
# class B(A):
#     pass
#     def method(self):
#         # super().method()
#         print('Hello , I am B')
# class C(A):
#     pass
#     def method(self):
#         # super().method()
#         print('Hello, I am C') 
# class D(B,C):
#     pass
#     # def method(self):
#     #     super().method()
#     #     print("Hello, I am D")  
# d = D()
# d.method()

# print(D.mro())

# # Diamond Problem -миксины
# #SOLID
# class Insects():
#     def __init__(self):
#         print('I am insect')
# class Bird:
#     def __init__(self):
#         print('I am a bird')
 

# class FlyMixin:
#     def fly(self):
#         print('I can fly')
# class Butterfly(Insects,FlyMixin):
#     pass
# class Hawk(Bird,FlyMixin):
#     pass
# class Eagle(Bird,FlyMixin):
#     pass
# class Pinguin(Bird):
#     pass

# hawk = Hawk()
# hawk.fly()


# eagle = Eagle()
# hawk.fly()
# ping = Pinguin()

# butterfly = Butterfly()
# butterfly.fly()


# class Vehicle:
#     pass
# class Gadgets:
#     pass
# class Shower:
#     pass
# class RadioMIxin:
#     def play_songs(self,station):
#         print(f'Playing some song on station {station}')

# class Car(Vehicle,RadioMIxin):
#     pass
# class Phone(Gadgets,RadioMIxin):
#     pass
# class  ShowerCabin(Shower,RadioMIxin):
#     pass

# car = Car()
# phone = Phone()
# showercabin = ShowerCabin()
# car.play_songs(station='Europa+')
# phone.play_songs(station='Makers Bootcamp')
# showercabin.play_songs(station="retro fm") 


"""Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""

class Auto:
    def ride(self):
        print('Riding on a ground')
class Boat:
    def swim(self):
        print('Floating on water')
class Amphibian(Boat,Auto):
    pass
amphibian = Amphibian()
amphibian.ride()
amphibian.swim()

"""Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""
# class RadioMixin:
#     def play_music(self,name):
#         print( f'Name: {name}')
# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')
# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')
# class Amphibian(Auto,Boat,RadioMixin):
#     pass
# some = Amphibian()
# some.play_music('My song')




"""Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
import datetime
class Clock:
    def current_time(self):
        print(datetime.datetime.now())
class Alarm:
    def switch_off(self):
        print('Switch off')
    def switch_on(self):
        print('Switch on')
class AlarmClock(Clock,Alarm):
    def set_alarmclock(self):
        print('Set alarm')
clock = AlarmClock()
clock.switch_on()
clock.switch_off()
clock.current_time()

"""Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

class Coder:
    experience = 
    count_code_time = 
    