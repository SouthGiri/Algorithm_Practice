import sys
input = sys.stdin.readline

# 1 2 3의 합으로 나타내기


# 1 : 1
# 2 : 2
# 3 : 4
# 4 : 7 / 3+1
# 5 : 13 / 4+1 3+2

t = int(input())
li = [0] * 11
li[1] = 1
li[2] = 2
li[3] = 4

for i in range(4, 11):
    li[i] = li[i-1] + li[i-2] + li[i-3]

for _ in range(t):
    num = int(input())
    print(li[num])