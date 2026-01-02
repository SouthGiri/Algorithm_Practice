import sys
input = sys.stdin.readline


ans = 0
data = []
sm1, sm2 = [], []
N = int(input())
for _ in range(N):
    data.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        sm1.append(data[i][0] + data[j][1])
        sm2.append(data[i][2] + data[j][3])

sm1.sort()
sm2.sort()

i, j = 0, len(sm2)-1

while i < len(sm2) and j >= 0:
    if -sm1[i] == sm2[j]:
        ii, jj = i+1, j-1
        while ii < len(sm2) and sm1[i] == sm1[ii]:
            ii += 1
        while jj >= 0 and sm2[j] == sm2[jj]:
            jj -= 1

        ans += (ii-i) * (j-jj)
        i, j = ii, jj
    elif -sm1[i] < sm2[j]:
        j -= 1
    else:
        i += 1

print(ans)