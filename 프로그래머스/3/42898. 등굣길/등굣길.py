def solution(m, n, puddles):
    answer = 0
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1
    
    for r, c in ((r, c) for r in range(1, n+1) for c in range(1, m+1)):
        if (r, c) == (1, 1):
            continue
        if [c, r] not in puddles:
            board[r][c] = (board[r-1][c] + board[r][c-1]) % 1000000007

    return board[r][c]