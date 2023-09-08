arr = [1,8,7,8,8,8,8]
key = 8
s=0
e=len(arr)-1

while(s<=e):
    mid = (s+e)//2
    if arr[mid] == key:
        firstOccurence = mid
        e = mid-1
    elif arr[mid]<key:
        s = mid+1
    else:
        e = mid - 1

s=0
e=len(arr)-1

while(s<=e):
    mid = (s+e)//2
    if arr[mid] == key:
        lastOccurence = mid
        s = mid+1
    elif arr[mid]<key:
        s = mid+1
    else:
        e = mid - 1

print("First Occurence:",firstOccurence)
print("Last Occurence:",lastOccurence)