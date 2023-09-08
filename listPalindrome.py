lst = []
 
print("Enter number of elements : ")

lst = list(map(int, input().split()))
 
i = 0
j = n-1
flag = -1
while(i<j):
    if(lst[i]!=lst[j]):
        print("Given List is Not Palindrome")
        flag = 1
        break
        exit
    else:
        i+=1
        j-=1    

if(flag== -1):
    print("Given List is Palindrome")