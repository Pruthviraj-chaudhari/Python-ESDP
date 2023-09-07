# a = int(input("Enter a Number: "))

# if(a<10):
#     print(a, "is Less than 10")
# else:
#     print(a, "is Greater than 10")
        

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# if (a==b):
#     print("Equal")
# else:
#     print("Not Equal")    

# age = int(input("Enter Your Age: "))
# if(age>18):
#     print("Eligible for voting")
# else:    
#     print("Not eligible for voting")


# num = int(input("Enter Number: "))
# if(num%2==0):
#     print(num, "is Even Number")
# else:    
#     print(num, "is Odd Number")


# a = int(input("Enter First Angle: "))
# b = int(input("Enter Second Angle: "))
# c = int(input("Enter Third Angle: "))

# sum = a+b+c

# if(sum == 180):
#     print("It is a Triangle")
# else:    
#     print("It is not a Triangle")


# math = int(input("Enter Marks obtained in Maths: "))
# phy = int(input("Enter Marks obtained in Physics: "))
# chem = int(input("Enter Marks obtained in Chemistry: "))
# sum = math+phy+chem
# percent = (sum/300)*100

# print("Total Marks Obtained: ",sum, "/300")
# print("Total Marks Obtained: ",percent)


# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if(a>b and a>c):
#     print(a,"is Greatest")
# elif(b>a and b>c):
#     print(b,"is Greatest")
# else:
#     print(c,"is Greatest")


# salary = int(input("Enter Salary: "))

# if(salary> 50000):
#     TA = (50000*30/100)
#     DA = (50000*20/100)
#     HRA = (50000*20/100)
#     print("Gross Salary: ", salary-TA-DA-HRA)
# elif(30000<salary and salary<50000):   
#     TA = (50000*15/100)
#     DA = (50000*15/100)
#     HRA = (50000*15/100)
#     print("Gross Salary: ", salary-TA-DA-HRA)
# else:
#     print("Gross Salary: ", salary)



# names = ["Nikhil", "Pruthvi", "Sandip", "Vivek"]
# print("Original List:", names)

# names.append("Gavande")
# print("After Append:", names)

# names.remove("Nikhil")
# print("After Remove:", names)


# a = int(input("Enter a Number: "))

# sum = 0

# while(a!=0):
#     sum += int(a % 10)
#     a /= 10

# print("Sum of Digit:", sum)



# def isLeapYear(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# year = int(input("Enter a year: "))

# if isLeapYear(year):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")



# a = int(input("Enter a Number: "))
# i = 1
# print("Numbers Perfectly Dividing", a)
# while(i <= (a/2)):
#     if(a % i == 0):
#         print(i)
#     i = i+1


# for i in range(0, 6):
#     for j in range(0, i):
#         print("*", end=" ")
#     print("")

# n = 6

# for i in range(0, n):
#     # Space
#     for j in range(0, n-i):
#         print(" ", end=" ")
#     # Star
#     for j in range(1, i+2):
#         print(j," ", end=" ")
#     print("")

# for i in range(0,n):
#     # space
#     for j in range(0, n-i-1):
#         print(" ", end=" ")
#     # star
#     for j in range(0, i-1):
#         print("*", end=" ")   
#     print("")     

import math
# Reverse Number
# n = int(input("Enter a Number: "))
# num = n
# rev = 0
# while(num != 0):
#     lastDigit = num%10
#     rev = (rev * 10) + lastDigit 
#     num//=10
# print(int(rev))

# Armstrong Number
# n = int(input("Enter a Number: "))
# digit = math.floor(math.log10(n)+1)
# num = n
# sum = 0
# while(num!=0):
#     last = num%10
#     sum += math.pow(last, digit)
#     num//=10

# if(sum == n):
#     print(n,"is an Armstrong Number")  
# else:
#     print(n,"is not an Armstrong Number") 


# print all armstrong
def isArmstrong(n):
    digit = math.floor(math.log10(n)+1)
    num = n
    sum = 0
    while(num!=0):
        last = num%10
        sum += math.pow(last, digit)
        num//=10

    return sum == n    

for i in range(100, 10000000000):
    if(isArmstrong(i)):
        print(i)