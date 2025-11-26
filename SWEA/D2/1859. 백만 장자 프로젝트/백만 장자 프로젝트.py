# 하루에 하나 구매
# 가장 비싼 날짜 이전까지 구매 / 비싼 날 판매
# 가장 비싼 날이 마지막날-2 라면 끝이고, 아니라면 슬라이싱해서 뒤에도 반복

t = int(input())
for i in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    
    res = 0
    argmax = lambda x : x.index(max(x))

    while True:
        max_idx = argmax(days)
        left, right = days[:max_idx+1], days[max_idx+1:]
        
        res -= sum(left[:-1])
        res += (len(left)-1) * left[-1]

        if len(right) < 2:
            break

        days = right
    
    print(f'#{i+1} {res}')