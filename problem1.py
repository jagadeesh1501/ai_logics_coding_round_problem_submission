
n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

result = []

for start, end in intervals:
    
    if not result:
        result.append([start, end])

    
    elif start <= result[-1][1]:
        result[-1][1] = max(result[-1][1], end)

    
    else:
        result.append([start, end])

for start, end in result:
    print(start, end)

# #sample input:
# Sample Input
# 4
# 1 3
# 2 6
# 8 10
# 15 18

# Sample Output
# 1 6
# 8 10
# 15 18
