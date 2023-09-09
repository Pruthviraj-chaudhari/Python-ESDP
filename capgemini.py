from collections import defaultdict
sem = int(input("Enter no of semester: "))

totalSemSubject = []

for i in range(0,sem):
    n = int(input(f"Enter no of subject in {i+1} semester: "))
    totalSemSubject.append(n)

dic = defaultdict(list)

for i in range(1, sem+1):
    print(f"Please enter marks in sem {i}: ")
    marks = list(map(int, input().split()))
    dic[i] = marks[:totalSemSubject[i-1]]

c = 1
for i in dic:
    print(f"Maximum mark in {c} semester: {max(dic[i])}") 
    c += 1       
