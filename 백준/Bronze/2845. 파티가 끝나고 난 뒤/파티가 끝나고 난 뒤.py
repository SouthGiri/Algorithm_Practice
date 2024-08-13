import sys
input = sys.stdin.readline

l, p = map(int, input().split())
li = list(map(int, input().split()))
for i in range(len(li)):
    print(li[i] - l*p, end=' ')