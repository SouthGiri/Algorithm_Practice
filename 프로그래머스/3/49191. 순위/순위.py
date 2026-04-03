def solution(n, results):
    answer = 0
    
    board = [[0] * (n+1) for _ in range(n+1)]
    
    for win, lose in results:
        board[win][lose] = 1
        board[lose][win] = -1
    
    for mid in range(1, n+1):
        for win in range(1, n+1):
            for lose in range(1, n+1):
                if board[win][mid] + board[mid][lose] == 2:
                    board[win][lose] = 1
                    board[lose][win] = -1

    for row in board[1:]:
        if row[1:].count(0) == 1:
            answer += 1
    
    return answer