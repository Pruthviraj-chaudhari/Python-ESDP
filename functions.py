# def Calculator(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul

# a  = int(input("Enter a Number: "))
# b  = int(input("Enter Second Number: "))
# sum, sub, div, mul = Calculator(a,b)
# print("Sum: ",sum)
# print("Sub: ",sub)
# print("Mul: ",mul)
# print("Div: ",div)


# def simpleInterest(n,p,r):
#     return (n*p*r)/100

# principal  = int(input("Enter Principle Amount: "))
# rate  = int(input("Enter Rate of Interest: "))
# year  = int(input("Enter No. of Years: "))

# print("Simple Interest: ", simpleInterest(year, principal, rate))


# def cube(num):
#     return num*num*num

# a  = int(input("Enter a Number: "))
# print("Cube of",a,"is", cube(a))


# def calculatePerimeter(l,b):
#     return 2*(l+b)
# def calculateArea(l,b):
#     return (l*b)
# l  = int(input("Enter Length of Reactangle: "))
# b  = int(input("Enter Breadth of Reactangle: "))
# print("Area:", calculateArea(l,b))
# print("Perimeter:", calculatePerimeter(l,b))


# def Power(x,y):
#     ans=1
#     for i in range(0,y):
#         ans*=x
#     return ans    
# x  = int(input("Enter Base: "))
# y  = int(input("Enter Power: "))
# print(x, "^", y, "=", Power(x,y))


# def isPrime(num):
#     for i in range(2, num//2+1):
#         if(num % i == 0):
#             return False      
#     return True    

# for i in range(1, 100):
#     if(isPrime(i) == True):
#         print(i,end=" ")


# def printFibonacci(num):
#     i = 0
#     a = 0
#     b = 1
#     next = a+b
#     while(next < num):
#         print(next, end=" ")
#         a = b
#         b = next
#         next = a+b
#         i+=1

# n = int(input("Enter n: "))
# print("\nFibonacci Series upto", n, ":")
# printFibonacci(n)


# def isEvenOdd(n):
#     if(n%2==0):
#         print("Even")
#     else:
#         print("Odd")

# n = int(input("Enter n: "))
# isEvenOdd(n)

# n = int(input("Enter Decimal Number: "))
# print("Equivalent Binary: ", bin(n))


def Add():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Addition is", a+b)

def Sub():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Subtraction is", a-b)

def Mul():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Multiplication is", a*b)

def Div():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print("Division is", a/b)

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def Power():
    ans=1
    x  = int(input("Enter Base: "))
    y  = int(input("Enter Power: "))
    for i in range(0,y):
        ans*=x
    print(x, "^", y, "=", ans)   


def Reverse():
    num = int(input("Enter a Number: "))
    n = num
    rev = 0
    last = -1
    while(n!=0):
        last = n % 10
        rev = (rev * 10) + last
        n//=10
    print("Reverse of",num, "=", rev) 

def isPalindrome():
    num = int(input("Enter a Number: "))
    n = num
    rev = 0
    last = -1
    while(n!=0):
        last = n % 10
        rev = (rev * 10) + last
        n//=10

    if(rev == num):
        print(num,"is Palindrome Number")  
    else:
        print(num,"is not Palindrome Number")  

def isArmstrong():
    import math
    num = int(input("Enter a Number: "))
    digit = math.floor(math.log10(num)+1)
    sum = 0
    n = num
    while(n != 0):
        bit = n%10
        sum+= math.pow(bit, digit)
        n//=10
    if(sum==num):
        print(num,"is an Armstrong Number")
    else:
        print(num,"is not an Armstrong Number")    


import sys

print('''
* * * * * * MENU * * * * * *
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Factorial Number
      6. Find Power
      7. Reverse
      8. Palindrome
      9. Armstrong
      10. Exit
''')

while True:
    ch = int(input("Enter Your Choice: "))

    if(ch==1):
        Add()
    elif ch==2:
        Sub()   
    elif ch==3:
        Mul()  
    elif ch==4:
        Div()  
    elif ch==5:
        n = int(input("Enter a Number: "))
        print("Factorial is", factorial(n) ) 
    elif ch==6:
        Power()  
    elif ch==7:
        Reverse()  
    elif ch==8:
        isPalindrome()  
    elif ch==9:
        isArmstrong()                  
    elif ch==10:
        sys.exit()
    else:
        print("Invelid Choice")    