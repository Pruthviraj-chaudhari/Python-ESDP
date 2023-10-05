print("The series is\n1+x/1+x^2/2.....+x^n/n")

x = int(input("Enter X:"))
n = int(input("Enter n:"))
sum = 1
for i in  range(1,n+1):
    sum += (x**i)/i
print(f"The sum of series of {x} in {n} range is {sum}")