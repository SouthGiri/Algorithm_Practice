N = int(input())
data = list(map(int, input().split()))

ans = 2e9
i, j = 0, N-1

while i < j:
	tmp = data[i] + data[j]
	if abs(tmp) < abs(ans):
		ans = tmp
	
	if tmp == 0:
		ans = 0
		break
	elif tmp > 0:
		j -= 1
	else:
		i += 1

print(ans)