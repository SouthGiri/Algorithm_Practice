from collections import deque

def check_accessible(row, col, container):
    if container[row-1][col] == '0' or container[row][col+1] == '0' or container[row][col-1] == '0' or container[row+1][col] == '0':
        return True
    return False


def solution(storage, requests):
    width = len(storage[0]) + 2
    height = len(storage) + 2

    container = [['0'] * width for _ in range(height)]
    for row in range(1, height-1):
        for col in range(1, width-1):
            container[row][col] = storage[row-1][col-1]

    for req in requests:
        if len(req) == 1: 
            for row in range(1, height-1):
                for col in range(1, width-1):
                    if container[row][col] == req and check_accessible(row, col, container):
                        container[row][col] = '1'

        else: 
            for row in range(1, height-1):
                for col in range(1, width-1):
                    if container[row][col] == req[0]:
                        container[row][col] = '1'

        queue = deque()
        queue.append((0, 0))
        visited = [[0] * width for _ in range(height)]

        while queue:
            row, col = queue.popleft()
            container[row][col] = '0'

            if not visited[row][col+1] and container[row][col+1] in ['0', '1']:
                queue.append((row, col+1))
                visited[row][col+1] = 1
            if not visited[row+1][col] and container[row+1][col] in ['0', '1']:
                queue.append((row+1, col))
                visited[row+1][col] = 1
            if not visited[row][col-1] and container[row][col-1] in ['0', '1']:
                queue.append((row, col-1))
                visited[row][col-1] = 1
            if not visited[row-1][col] and container[row-1][col] in ['0', '1']:
                queue.append((row-1, col))
                visited[row-1][col] = 1

    result = 0
    for row in range(1, height-1):
        for col in range(1, width-1):
            if container[row][col] not in ['0', '1']:
                result += 1

    return result