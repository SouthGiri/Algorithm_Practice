# iter 마다 슬라이싱으로 window 확인, fir 계산, fir == mid 인 경우 sec 계산, res += fir-sec, mid += 2
# fir : max, sec : mid 빼고 max (index 필요 없음)

max_idx = lambda x : x.index(max(x))
for i in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    
    res = 0
    mid = 2
    while mid < n-2:
        window = buildings[mid-2:mid+3]
        fir_idx = max_idx(window)
        if fir_idx == 2:
            sec = max(window[:2] + window[3:]) # sec 은 인덱스가 아닌 val
            res += window[2]-sec
            mid += 2
        
        mid += 1
    print(f'#{i+1} {res}')
