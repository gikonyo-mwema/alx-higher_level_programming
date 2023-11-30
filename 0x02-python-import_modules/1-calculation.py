#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

add(a, b)
print(f'{a} + {b} = {a + b}')

sub(a, b)
print(f'{a} - {b} = {a - b}')

mul(a, b)
print(f'{a} * {b} = {a * b}')

div(a, b)
print(f'{a} / {b} = {int(a / b)}')
