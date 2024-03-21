import sys
input = sys.stdin.readline

# function R : reverse array
# D : drop index 0
# if array is empty : D() -> error

def R(arr):
    global reverse_flag
    reverse_flag = not reverse_flag

def D(arr):
    try:
        if reverse_flag:
            arr.pop()
        else:
            arr.pop(0)
    except:
        global error_flag
        error_flag = True
    
t = int(input())
for _ in range(t):
    reverse_flag = False
    error_flag = False
    func = list(input().rstrip().replace('RR', ''))
    n = int(input())
    # sep : ,
    li = list(map(int, input()[1:-2].replace(',', ' ').split()))

    for i in range(len(func)):
        if func[i] == 'R':
            R(li)
        else:
            D(li)

    if error_flag:
        print('error')
    else:
        if reverse_flag:
            li = li[::-1]
        print('[' + ','.join(map(str, li)) + ']')
    
