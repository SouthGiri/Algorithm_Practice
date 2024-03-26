import sys
input = sys.stdin.readline

# 세로로 채우는 경우부터
# n=1 1
# n=2 2
# n=3 3-1 1-2 3
# n=4 4-1 2-3 0-1 5
# n=5 5-1 3-4 1-3 8
# n=6 6-1 4-5 2-
n = int(input())
li = [0] * 1001
li[1] = 1
li[2] = 2
li[3] = 3
for i in range(4, len(li)):
    li[i] = (li[i-1] + li[i-2]) % 10007

print(li[n])