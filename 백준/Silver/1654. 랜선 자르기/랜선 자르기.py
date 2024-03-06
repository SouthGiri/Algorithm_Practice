k, n = map(int, input().split())
cables = []

for _ in range(k):
    cables.append(int(input()))

start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2
    count = sum(cable//mid for cable in cables)
    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)