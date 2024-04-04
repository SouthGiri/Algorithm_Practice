import sys
input = sys.stdin.readline

# greedy?
# first : smallest end time
# after : before end time <= after start

meet = []

n = int(input())
for _ in range(n):
    start, end = map(int,input().split())
    meet.append([start, end])

meet.sort(key=lambda x : (x[1], x[0]))

num = 1
end_time = meet[0][1]

for i in range(1, n):
    if meet[i][0] >= end_time:
        num += 1
        end_time = meet[i][1]

print(num)