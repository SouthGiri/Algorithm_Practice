import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
srt = sorted(list(set(line)))

dic = dict()
for i in range(len(srt)):
    dic[srt[i]] = i

for i in line:
    print(dic[i], end=' ')