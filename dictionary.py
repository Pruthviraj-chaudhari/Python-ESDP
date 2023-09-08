# d = {}

# for i in range(0,100000000000000000):
#     d[i] = i*i
# # print(d.values())
# # print(d.keys())
# # print(d.items())

# for items in d:
#     print("Numbers:",items, " Squares:",d[items])


ls = [10,10,20,20,20,30,40,10]

freq = {}

for element in ls:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1    

print(freq)