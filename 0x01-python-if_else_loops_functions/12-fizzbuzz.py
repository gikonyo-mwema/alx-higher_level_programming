#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            end_char = " " if i < 100 else "\n"
            print("FizzBuzz", end=end_char)
        elif i % 3 == 0:
            end_char = " " if i < 100 else "\n"
            print("Fizz", end=end_char)
        elif i % 5 == 0:
            end_char = " " if i < 100 else "\n"
            print("Buzz", end=end_char)
        else:
            end_char = " " if i < 100 else "\n"
            print(i, end=end_char)

