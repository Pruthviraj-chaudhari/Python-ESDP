# ls = [0, 1, 153, 370, 371, 407]

# MAX & MIN ELEMENT
# min = ls[0]
# max = ls[0]
# for i in ls:
#     if(i<min):
#         min = i
#     if(i>max):
#         max = i
# print("Max:", max)    
# print("Min:", min)    

# SECOND MAXIMUM
# max = ls[0]
# second = ls[0]
# for i in ls:
#     if(i>max):
#         second = max
#         max = i
# print("Max:", second)    





# freq = {}

# for element in ls:
#     if element in freq:
#         freq[element] += 1
#     else:
#         freq[element] = 1    

# print(freq)

# visited = []
# for i in ls:
#     c = 0
#     if i not in visited:
#         for j in ls:
#             if(i==j):
#                 c+=1

# import math
# def armStrong(n):
#     num = n
#     digit = math.floor(math.log10(n)+1)
#     sum = 0
#     while(num!=0):
#         last = num%10
#         sum += math.pow(last, digit)
#         num//=10
#     return sum==n   

# for i in ls:
#     if(armStrong(i)):
#         print(i, end=" ")

ls = [1, 2,3,4,5]
# REVERSE
# i=0
# j=len(ls)-1

# while(i<j):
#     temp = ls[i]
#     ls[i] = ls[j]
#     ls[j] = temp
#     i+=1
#     j-=1
# print(ls)

ls2 = ls
count=0
for i in range(len(ls) - 1, -1, -1):
    ls[count] = ls2[i]
    count+=1

print(ls2)    
