num = int(input("Enter Number: "))

sum=0
temp = num
while(temp!=0):
    bit = temp%10
    sum+=bit
    temp//=10

if(sum>=20 and sum<=30):
    print("Difference of 5: ", (sum-5))
else:
    print("Real Sum: ",sum)    
