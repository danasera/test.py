from os import read, write
from typing import BinaryIO, Text


file1 = open('makers.txt','r')
print(file1.read())

r - read
r+ read + write
w - write
w+ - read + write
a - append
a+ - append + read
x - write
b - Binary
t - Text
rt -> r 
