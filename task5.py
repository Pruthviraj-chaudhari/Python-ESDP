import math

def isArmstrong(a):
    sum=0
    power = math.floor(math.log10(a)+1)
    num=a
    while(num!=0):
        bit = num%10
        sum += math.pow(bit, power)
        num//=10

    if sum==a: return True
    else: return False    


lower = int(input("Enter Lower Bound: "))
upper = int(input("Enter Upper Bound: "))

for i in range(lower,upper):
    if(isArmstrong(i)):
        print(i)
        