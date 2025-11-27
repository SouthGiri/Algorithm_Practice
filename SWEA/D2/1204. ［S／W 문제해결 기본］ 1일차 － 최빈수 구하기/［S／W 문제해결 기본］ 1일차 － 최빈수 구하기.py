T = int(input())
for _ in range(T):
    case = int(input())
    arr = list(map(int, input().split()))
    freq = dict()
    for score in arr:
        if score not in freq:
            freq[score] = 1
        else:
            freq[score] += 1
    ans = max(freq, key=freq.get)
    print(f'#{case} {ans}')