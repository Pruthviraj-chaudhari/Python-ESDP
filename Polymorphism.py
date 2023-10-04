# Method Overloading

# class Parent:
#     def properties(self):
#         print("Cash, Gold")

#     def bike(self):
#         print("Splender +")


# class Child(Parent):
#     def bike(seilf):
#         print("Average")


# c = Child()
# c.properties()
# c.bike()


# class A:
#     def show(self):
#         print("Class A")

# class B:
#     def show(self):
#         print("Class B")

# class C(A,B):
#     def showC(self):
#         print("Class C")


# obj = C()
# obj.showC()
# obj.show()


# class Parent:
#     def __init__(self):
#         print("Parent Constructor")

# class Child(Parent):
#     def __init__(self):
#         print("Child Constructor")

# c = Child()        


class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A,B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()