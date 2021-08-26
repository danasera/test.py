# find(string), rfind(string)
# string = 'Makers Bootcamp'
# print(string.rfind('Make'))


# index(string), rindex (string)
string = 'Makers Bootcamp Boot Boot'



# replace(pattern, replace_pattren)
string = 'Makers Bootcamp'
string.replace('camp', 'rock')
print(string)



x = 20 

while True:
    number = int(input('Введите число'))
    if x == number:
        print('Выигрыш!')
        break
print('Try again!')    
# split (symbol) -> list
string = 'Makers Bootcamp'
print(string.split('*'))



full_name = input ('Enter name and lastname: ').split(',')
name = full_name[0]
last_namen = full_name[-1]



 








#  Task

# 1
data = input('Введите имя, фамлию и возраст через пробел:\n').split()
name = data[0]
last_name = data[1]
age = data[-1]

name = name.lower().replace('a', '')
last_name = '*'.join(list(last_name))
print(name + last_name * int(age))


# 2
string

