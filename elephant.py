a = int(input())
ans = 0

while(a>0):
    if(a%5>0 and a>=5):
        ans += a//5
        a%=5
    elif(a%4>0 and a>=4):
        ans += a//4
        a%=4

    elif(a%3>0 and a>=3):
        ans += a//3
        a%=3

    elif(a%2>0 and a>=2):
        ans += a//2
        a%=2

    else:
        ans += a
        a=0

print(ans-1)