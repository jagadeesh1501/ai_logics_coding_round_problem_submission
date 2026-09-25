n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

result = []
carry = 0

i = 0

while i < n or i < m or carry:
    
    if i < n:
        x = a[i]
    else:
        x = 0

    if i < m:
        y = b[i]
    else:
        y = 0

    total = x + y + carry

    result.append(total % 10)
    carry = total // 10

    i += 1

print(*result)

# Sample Input 1

# 3
# 2 4 3
# 3
# 5 6 4

# Sample Output 1
# 7 0 8
