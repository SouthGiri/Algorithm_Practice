def bin_sear(data, target):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start+end) // 2
        if data[mid] == target:
            return True
        if data[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return False

    
N = int(input())
data = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

data.sort()
for card in cards:
    if bin_sear(data, card):
        print(1, end=' ')
    else:
        print(0, end=' ')