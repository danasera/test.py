# def hello_makers():
#     print('Hello ,Makers!')

# #хранить фунцйии в переменных
# makers = hello_makers
# print(id(makers))
# print(id(hello_makers))

# #определить функйии внутри другой фунции
# def outer_func():
#     def inner_func():
#         print('Hello, Makers')
#     inner_func()

# outer_func()

# #передавать  функции в качестве аргумента и возвращать и из друнмх фунции
# def main_func(func):
#     print(f'I use function{func} as argument')
#     func()
#     return func

# def hello_makers():
#     print('Hello,Makers')

# main_func(hello_makers)


#Decorator
# def func1():
#     print('A am called inside other function')

# def func2(func):
#     print("I'll do something before func calling")
#     func()


# def func3():
#     print('Helllo,Makers!!!!!!!')

# func2(func3)



# def decorator(func):
#     print("I am a function decorator")
#     def wrapper():
#         print("I am a function-wrapper")
#         print("We should call wrapper-function")
#         func()
#         print('I am out of wrapper')

#     return wrapper
# @
# @decorator
# def hello_bootcamp():
#     print("This is Boootcamp")

# hello_bootcamp()



# def check_password(func):
#     def wrapper(password):
#         return func(password).strip()
#     return wrapper

# @check_password
# def get_info(password):
#     return password
# password = input("Enter your info:")
# print(get_info(password))
  

# @check_password
# def get_email():
#     email = input("Enter email: ")
#     return email

# # print(get_info(password))


# def bread(func):
#     def wrapper(*args):
#         print('</-------\>')
#         func(*args)
#         print('</-------\>')
#     return wrapper
# def ingredients(func):
#     def wrapper(*args):
#         print('#tomato#')
#         func(*args)
#         print('--salad---')
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(*fillers):
#     for filler in fillers:
#         print(filler)
#     print(filler)
# get_sandwich('--hum--','**sausage**','&Ketchup&')
# get_sandwich('--hum--')


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print(f"see what i got:{args}")
#         print(f"see what i got:{kwargs}")
#         func(*args,**kwargs)
        
#     return wrapper

# @decorator
# def func_without_params():
#     print("I am a poor func without params")
# func_without_params()   

# @decorator
# def func_with_params(name,last_name):
#     print("I am happy func with params")
#     print(f"Hello, {name} {last_name}")

# func_with_params('sam',last = 'white')
# # func_with_params()



# def func(x):
#     return x * 2


# func(10)
# func('2')
# func([2, 4])


# def func():
#     pass

# class a:
#     pass
# print(type(func))
# print(type(a))

# 1. Function belong to peremennaia

# def my_func():
#     print("Hello world")

# func1 = my_func
# func1()


# 2.Фунцуия можкт принимать другую в качесиве аргумента
# -Функция  может возвращать фукцию в качестве результата
# -Фунцция можкт определять анутри себя другие функции


# def  func():
#     def func2():
#         a = 10
#     pass
# def func1(x):
#     pass
# def func2():
#     pass

# class A:
#     pass
# func1(23)
# func1('gigi')
# func1({})
# func1(func2)
# func1(A)
# Декораторы - это фунцйии , лоя расширения возможесией друших фунцции , without changing the code.
# decorators  должке приниать фунцию, добавлять в нее фунционал и возвращать измененную функцию 

# def decorators(function):
#     def wrapper(*args,**kwargs):
#         print('Code before calling')
#         print('function is calling')
#         res =function(*args,**kwargs)
#         print("code after calling")
#         return res
#     return wrapper
# @decorators
# def my_func1():
#     print('Hello World')
# # my_func1() #wrapper()
# @decorators
# def my_func2(x,y):

#     return x * y

# print(my_func2(20,10))
# my_func1 = decorators(my_func1)
# my_func1 = wrapper
# my_func1()
# decorator(my_func1)
# def decorator(func):
#     return func - do not work
# def summarize(x,y):
# записывает в файл , какая фунция была вызвана , время , c какими аргументами

# def decorator(func):
#     import datetime
#     def wrapper(*args,**kwargs):
#         current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#         func(*args,**kwargs)
#         with open('log.txt','w') as file:
#             file.write(f'{func._name_} \n')
#             file.write(f'calling{current_time} \n')
#             file.write(f'args:{args}\n')
#             file.write(f'Kwargs: {kwargs}\n')
#             file.write('---------------\n')
#     return wrapper
# def timer(func):
#     import time
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         end = time.time()
#         working_time = end - start
#         print(f'Время выполнения фунцйии{func.__name__}:{working_time}sec')
#     return wrapper

def timer(count=1):
    import time
    def decorator(func):
        def wrapper(*args,**kwargs):
            total_time = 0
            for i in range(count):
                start = time.time()
                func(*args,**kwargs)
                end = time.time()
                working_time = end - start
                total_time +=working_time
            avg_time = total_time/ count
            print(f'Среднее время выполнения фунцйии{func.__name__}:{avg_time}sec')
        return wrapper
    return decorator




@timer(count=100)
def func1():
    print('Hello world')
@timer()
def func2(x,y):
    return x + y


@timer(count=5)
def func3(url):
    import requests
    return requests.get(url)

func1()
func2(20,25)

func3('https://vesti.kg/')
func2(x=10,y=20)


# Декоратор, замеряющий время выполнения функции(зв n повторений)



