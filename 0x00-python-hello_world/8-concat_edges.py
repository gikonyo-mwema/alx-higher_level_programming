#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = '-'.join(str.split()[2].split()[1:3]) + " with Python"
print(str)
