import sys
input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    if line.count(0) == 3:
        break
    
    else:
        line.sort()
        if line[2]**2 == line[0]**2 + line[1]**2:
            print('right')
        else:
            print('wrong')