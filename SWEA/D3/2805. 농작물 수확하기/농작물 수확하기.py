T = int(input())
for case in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0

    mid = N//2
    start = end = mid
    
    for i in range(N):
        ans += sum(board[i][start:end+1])
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{case} {ans}')