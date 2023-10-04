# class MyClass:
#     def __init__(self):
#         print("First Constructor")
#     def __init__(self):
#         print("Second Constructor")
#     def __init__(self):
#         print("Third Constructor")       # This constructor will be called because of overriding (Everytime last wala)

# obj1 = MyClass()


# class MyClass:
#     def __init__(self):
#         print("First Constructor")
#     def __init__(self, a):
#         print("Second Constructor")
#     def __init__(self, a, b):
#         print("Third Constructor",a,b)      

# # obj1 = MyClass()     # Error --> (Everytime last wala) but last wala has arguments
# obj2 = MyClass(1,2)     # solution --> pass arguments
     

class MyClass:
    def __init__(self):
        print("First Constructor")
    def __init__(self, a=None):
        print("Second Constructor", a)
    def __init__(self, a=None, b=None):
        print("Third Constructor",a,b)       

obj1 = MyClass()    # no errors
obj2 = MyClass(1)    # no errors
obj2 = MyClass(1, 2)    # no errors