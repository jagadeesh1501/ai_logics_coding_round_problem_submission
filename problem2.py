n = int(input())
arr = list(map(int, input().split()))
k = int(input())

left = 0
best_length = 0
best_start = 1

for right in range(n):

    while max(arr[left:right + 1]) - min(arr[left:right + 1]) > k:
        left += 1

    length = right - left + 1

    if length > best_length:
        best_length = length
        best_start = left + 1

print(best_length, best_start)