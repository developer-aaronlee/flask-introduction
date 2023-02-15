"""Command Line"""
"""print working directory - current location: pwd"""
"""list - list out file/fold in current directory: ls"""
"""change directory - change current directory: cd <folder name>"""
"""make directory - create a new directory: mkdir <folder name>"""
"""make file - create a new file: touch <file name.file type>"""
"""remove file - delete a file: rm <file name.file type>"""
"""one step up - go back to parent folder: cd .."""
"""remove folder - delete a folder: rm -rf <folder name>"""


"""Functions as First Class Objects: Passing & Nesting Functions"""

import time


# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2


# def calculate(calc_func, n1, n2):
#     return calc_func(n1, n2)
#
#
# print(calculate(add, 2, 3))
# print(calculate(multiply, 2, 3))


# def outer_func():
#     print("outer")
#
#     def inner_func():
#         print("inner")
#
#     inner_func()
#
#
# outer_func()


# def outer_func():
#     print("outer")
#
#     def inner_func():
#         print("inner")
#
#     return inner_func
#
#
# nested_func = outer_func()
# print(nested_func)
# nested_func()
# print(nested_func())


# def delay_func(func):
#
#     def wrapper_func():
#         time.sleep(3)
#         func()
#     return wrapper_func
#
#
# @delay_func
# def say_hello():
#     print("hello")
#
#
# def say_bye():
#     print("bye")
#
#
# say_hello()
# decorated_func = delay_func(say_bye)
# decorated_func()


# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print("start")
#         num = func(*args, **kwargs)
#         print("end")
#         return num
#
#     return wrapper
#
#
# @decorator
# def text(x):
#     print(x)
#
#
# @decorator
# def number(x, y):
#     print(x)
#     return y
#
#
# text(5)
# result = number(5, 6)
# print(result)


# def delay(func):
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         total = time.time() - start
#         print("Time:", total)
#         return result
#
#     return wrapper
#
#
# @delay
# def fast():
#     for x in range(10000000):
#         pass
#
#
# @delay
# def slow():
#     for x in range(100000000):
#         pass
#
#
# fast()
# slow()


# class User:
#
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_authenticated_decorator(func):
#
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             func(args[0])
#
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"this is {user.name}'s blog post.")
#
#
# new_user = User("abc")
# new_user.is_logged_in = True
# create_blog_post(new_user)


def decorator(func):

    def wrapper(*args, **kwargs):
        print(f"You called function: {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")

    return wrapper


@decorator
def test(x, y, z):
    return x + y + z


test(1, 2, 3)

