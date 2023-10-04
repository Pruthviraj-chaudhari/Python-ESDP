
def countDigit(num):
    sum=0
    temp = num
    while(temp!=0):
        sum+=1
        temp//=10
    return sum    

digit = 0

while(digit < 5):
    num = int(input("Enter Number: "))
    digit = countDigit(num)
    if(digit>=5):
        print("Enter Upto 5 digit number") 
        break
    else:
        print("Ok✅ Its less than 5 digit")

