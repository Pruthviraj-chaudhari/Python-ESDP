def printTable(num):
    print("\nTable of",num, "👍")
    for i in range(1,11):
        print(i*num)
        

a = int(input("Enter Lower Bound: "))
b = int(input("Enter Upper Bound: "))

for i in range(a,b+1):
        printTable(i)