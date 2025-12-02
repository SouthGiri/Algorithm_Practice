N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort(reverse=True)
res = []

for i in range(N):
    res.append(data[i]*(i+1))

print(max(res))