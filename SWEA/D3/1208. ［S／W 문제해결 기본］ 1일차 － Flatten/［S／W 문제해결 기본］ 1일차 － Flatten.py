
import heapq

for case in range(1, 11):
	swap = int(input())
	boxes = list(map(int, input().split()))
	avg = sum(boxes) // len(boxes)
	max_h, min_h = [], []
	ans = 0
	for box in boxes:
		if box > avg:
			heapq.heappush(max_h, -box)
		else:
			heapq.heappush(min_h, box)
			
    # max_heap 에서 꺼내서 -1 하고 min에서 꺼내서 +1 하고 각자 다시 넣기
	for i in range(swap):
		largest = -heapq.heappop(max_h)
		smallest = heapq.heappop(min_h)
		heapq.heappush(max_h, -largest+1)
		heapq.heappush(min_h, smallest+1)
	
	# 최종에는 max_h, min_h 에서 꺼내서 차를 구하면 ans
	ans = -heapq.heappop(max_h) - heapq.heappop(min_h)
	
	print(f'#{case} {ans}')