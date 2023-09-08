a = int(input())
b = int(input())
 
first = a %10
 
while(b>0):
    if((a % 10) != 0):
        a = a-1
    else:
        a = a//10
        
    b = b-1
    
print(a)