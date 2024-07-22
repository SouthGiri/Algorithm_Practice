import sys
input = sys.stdin.readline

import math

i = 1
while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    
    print('Triangle #{}'.format(i))
    i += 1
    if c == -1:
        ans = math.sqrt(a**2 + b**2)   
        print('c = %0.3f' %ans)

    if a == -1:
        ans = c**2 - b**2
        if ans <= 0:
            print('Impossible.')
        else:
            print('a = %0.3f' %math.sqrt(ans))

    if b == -1:
        ans = c**2 - a**2
        if ans <= 0:
            print('Impossible.')
        else:
            print('b = %0.3f' %math.sqrt(ans))
    print()
