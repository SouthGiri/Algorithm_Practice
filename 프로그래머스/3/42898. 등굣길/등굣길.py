def solution(m, n, puddles):
    
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1
    
    for row, col in ((r, c) for r in range(1, n+1) for c in range(1, m+1)):
        if (row, col) == (1, 1):
            continue
        
        if [col, row] in puddles:
            continue
            
        board[row][col] = (board[row-1][col] + board[row][col-1]) % 1_000_000_007
    
    return board[n][m]