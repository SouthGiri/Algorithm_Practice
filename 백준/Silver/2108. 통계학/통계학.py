import sys
input = sys.stdin.readline

n = int(input())
nums = []
count = dict()
for _ in range(n):
    nums.append(int(input()))
    if nums[-1] in count:
        count[nums[-1]] += 1
    else:
        count[nums[-1]] = 1

nums.sort()

print(round(sum(nums)/n))
print(nums[n//2])

freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)
numbers.sort()
if len(numbers) == 1:
    print(numbers[0])
else:
    print(numbers[1])

print(nums[-1] - nums[0])