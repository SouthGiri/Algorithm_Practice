import sys
input = sys.stdin.readline

tri_num = [i*(i+1)//2 for i in range(1, 46)]
ans = [0] * 1001

for i in tri_num:
    for j in tri_num:
        for k in tri_num:
            num = i+j+k
            if num <= 1000:
                ans[num] = 1

n = int(input())
for _ in range(n):
    print(ans[int(input())])
