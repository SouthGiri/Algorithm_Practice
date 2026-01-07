import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

ans = 0

if boxes[0] > cranes[0]:
    ans = -1
else:
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane < boxes[-1]:
                    continue

                if crane >= box:
                    boxes.remove(box)
                    break
        
        ans += 1
            
print(ans)