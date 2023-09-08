# d = {}

# for i in range(0,100000000000000000):
#     d[i] = i*i
# # print(d.values())
# # print(d.keys())
# # print(d.items())

# for items in d:
#     print("Numbers:",items, " Squares:",d[items])


# FREQUENCY in DICTIONARY
# ls = [10,10,20,20,20,30,40,10]
# freq = {}
# for element in ls:
#     if element in freq:
#         freq[element] += 1
#     else:
#         freq[element] = 1    
# for i in freq:
#     print("Element:", i, " Frequency:",freq[i])


# FREQUENCY USING DEFAULTDICT
# from collections import defaultdict
# freq = defaultdict(int
# for i in ls:
#     freq[i] += 1
# print(freq)    


# FREQUENCY USING COUNTER
# from collections import Counter
# print(Counter(ls))


# Questions
# from collections import defaultdict
# ls = [10,9, 1, 21, 29, 3, 15]
# d = defaultdict(list)
# for i in ls:
#     d[i//10].append(i)
# print(d)


# ZIG-ZAG TRAVERSAL IN 2-D LIST

ls = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
] 

for i in range(0, len(ls)):
    for j in range(0, len(ls[i])):
        if(i%2==0):
            print(ls[j][i], end=" ")
        else:
            print(ls[3-j][i], end=" ")    
    print(" ")    