import sys
input = sys.stdin.readline

t = int(input())
a,b,c=0,0,0
while t > 0:
    if t >= 300:
        a +=1
        t -= 300
    elif t >= 60:
        b += 1
        t -= 60
    elif t >= 10:
        c += 1
        t -= 10
    else:
        print(-1)
        break

else:
    print(a,b,c)