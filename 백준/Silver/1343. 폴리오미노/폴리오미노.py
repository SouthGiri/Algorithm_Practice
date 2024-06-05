import sys
input = sys.stdin.readline


board = input().rstrip()
i = 0
ans = ''
while i < len(board):
    if board[i:i+4].count('X') == 4:
        ans += 'AAAA'
        i += 4
    elif board[i:i+2].count('X') == 2:
        ans += 'BB'
        i += 2
    elif board[i] == '.':
        ans += '.'
        i += 1
    else:
        print(-1)
        break

else:
    print(ans)