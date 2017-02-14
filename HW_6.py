import time
import sys
import random

# Задача №2 ("""Реализовать декоратор, который измеряет скорость
             # выполнения функций. Написать три разные функции, 
             # задекорировать их и проверить)

 
def time_decorator(func): # Задача №2 ("""Реализовать декоратор, который измеряет скорость
                          # выполнения функций. Написать три разные функции, 
                          # задекорировать их и проверить)

    def inner (*arg):
        startTime = time.time()
        print("Function name is", func.__name__)
        func(*arg)
        print ("Elapsed time: {:.6f} sec".format(time.time() - startTime))

    return inner
    

@time_decorator
def Printer(*arg):
    print ("My text is", arg * 2)

@time_decorator
def my_sum(*arg):
    print ("Sum of my arg is", sum(arg))


my_sum(1, 4, 288)
Printer("Hi world!")



# Задача №1 
# (Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана)

def stop_function (func):
    def inner(*arg):
        print ("Функция {} не будет вызвана" .format(func.__name__))
    return inner

@stop_function
def my_mult(*arg):
    print ("Sum of my arg is", mult(arg))

my_mult(1, 4, 288)

# Задача №3
#(Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100)

x = (i for i in range (0,101) if i % 2 == 0)
print (list(x))

# Задача №4
# (Написать генератор, который возвращает бесконечную последовательность случайных чисел,
# таких что следующее не меньше прошлого)

class My_generator_of_infinite():
   
    def __init__(self, start =0):
        self.start = start
       
    def __iter__(self):
        return self

    def __next__(self): 

        self.nextnumber =  random.randint(0, sys.maxsize) # почему не работает math.inf? maxsize же не бескоечное число...

        if self.start > self.nextnumber:
           while self.start > self.nextnumber:
                 self.nextnumber =  random.randint(0, sys.maxsize) #как сделать цикл подсмотрела

        self.start = self.nextnumber
        return self.nextnumber


y = My_generator_of_infinite()
print(y.__next__())
print(y.__next__())

# Задача №5
# Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день

import datetime

def My_generator_of_date(year, month, day):
    input_data = datetime.date(year, month, day)
    while True:
        input_data += datetime.timedelta(days=1)
        yield input_data
    

   

a = My_generator_of_date (2017, 2, 14)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a)) 
