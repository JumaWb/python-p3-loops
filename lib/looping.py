#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
  squared_list = [x ** 2 for x in int_list]
  return squared_list
int_list = [2, 4, 6, 8, 10]
squared_list = square_integers(int_list)
print(squared_list)
  

def fizzbuzz():
  for i in range(1, 101):
      if i % 3 == 0 and i % 5 == 0:
          print("FizzBuzz")
      elif i % 3 == 0:
          print("Fizz")
      elif i % 5 == 0:
          print("Buzz")
      else:
          print(i)

fizzbuzz()