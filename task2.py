def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def seriesSum(x, n):
    result = 1.0  
    for i in range(1, n + 1):
        term = (x ** i) / factorial(i)
        result += term
    return result


x = float(input("Enter x: "))
n = int(input("Enter n: "))

ans = seriesSum(x, n)
print(f"The sum of the series is: {ans}")
