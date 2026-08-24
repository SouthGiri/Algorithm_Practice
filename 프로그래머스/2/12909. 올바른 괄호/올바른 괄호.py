def solution(s):
    answer = True
    
    stack = []
    
    for letter in s:
        if letter == '(':
            stack.append(letter)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    
    if stack:
        return False

    return True